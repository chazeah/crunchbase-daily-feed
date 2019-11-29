import pytz
from bs4 import BeautifulSoup
from datetime import (
    datetime,
)
from django.core.management.base import BaseCommand

from scraper.models import Result
from content_parser.models import CBDPost


class Command(BaseCommand):
    def handle(self, *args, **options):
        to_parse = Result.objects.filter(has_been_parsed=False)
        if to_parse.count() == 0:
            print('No new scraper results to parse.')
            return

        def mark_as_parsed(result):
            result.has_been_parsed = True
            result.parsed_at = datetime.now(pytz.utc)
            result.save()

        print('Parsing new scraper results ({})...'.format(to_parse.count()))
        for result in to_parse.iterator():
            soup = BeautifulSoup(result.response_text, 'html.parser')
            # We have to use a fairly indirect way of finding the pub date.
            share_link = soup.find('a', title='Share on Twitter')
            pub_date = share_link.find_parent('tr').find('td').get_text(strip=True)

            if not pub_date:
                # Mark post as parsed and move on.
                print('No publish date found in Result (ID: {})'.format(result.id))
                mark_as_parsed(result)
                continue

            try:
                pub_date_obj_raw = datetime.strptime(pub_date, "%B %d, %Y")
                pub_date_obj = pub_date_obj_raw.replace(tzinfo=pytz.UTC)
                print('Publish date for Result found (ID: {}, Date: {})'.format(
                    result.id,
                    pub_date_obj,
                ))
            except ValueError:
                print('Failed to parse publish date in Result (ID: {})'.format(result.id))
                mark_as_parsed(result)
                continue

            # Only create Post object if entry doesn't already exist.
            existing_posts = CBDPost.objects.filter(published_at=pub_date_obj)
            if existing_posts.exists():
                print('Post for this date (Result ID: {}) already exists (ID: {})'.format(
                    result.id,
                    existing_posts.first().id,
                ))
                mark_as_parsed(result)
                continue

            content_root = soup.find('h2').find_parent('td')
            if not content_root:
                print('Failed to find content root for Result (ID: {})'.format(result.id))
                mark_as_parsed(result)
                continue

            for tag in content_root():
                for attribute in ['class', 'id', 'style']:
                    del tag[attribute]

            body_content = ''
            for child in content_root.contents:
                body_content += str(child)

            title = 'Crunchbase Daily ({})'.format(pub_date_obj.strftime('%b %-d'))

            post = CBDPost.objects.create(
                title=title,
                body_content=body_content,
                published_at=pub_date_obj,
            )

            print('Parsed Result (ID: {}), created CBDPost (ID: {})'.format(
                result.id,
                post.id,
            ))
            mark_as_parsed(result)

        print('Complete')
