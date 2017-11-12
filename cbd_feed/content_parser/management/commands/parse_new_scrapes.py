from bs4 import BeautifulSoup
from datetime import (
    datetime,
    timezone,
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
            result.parsed_at = datetime.now(timezone.utc)
            result.save()

        print('Parsing new scraper results ({})...'.format(to_parse.count()))
        for result in to_parse.iterator():
            soup = BeautifulSoup(result.response_text, 'html.parser')
            pub_time = soup.find(property='article:published_time')

            if not pub_time:
                # Mark post as parsed and move on.
                print('No publish date found in Result (ID: {})'.format(result.id))
                mark_as_parsed(result)
                continue

            try:
                pub_time_obj = datetime.strptime(
                    pub_time.attrs['content'],
                    '%Y-%m-%d %H:%M:%S %z'
                )
                print(pub_time_obj)
            except ValueError:
                print('Failed to parse publish date in Result (ID: {})'.format(result.id))
                mark_as_parsed(result)
                continue

            # Only create Post object if entry doesn't already exist.
            existing_posts = CBDPost.objects.filter(published_at=pub_time_obj)
            if existing_posts.exists():
                print('Post for this date (Result ID: {}) already exists (ID: {})'.format(
                    result.id,
                    existing_posts.first().id,
                ))
                mark_as_parsed(result)
                continue

            content_root = soup.find('td', {'class': 'cbForwardText'})
            for tag in content_root():
                for attribute in ['class', 'id', 'style']:
                    del tag[attribute]

            body_content = ''
            for child in content_root.contents:
                body_content += str(child)

            title = 'Crunchbase Daily ({})'.format(pub_time_obj.strftime('%b %-d'))

            post = CBDPost.objects.create(
                title=title,
                body_content=body_content,
                published_at=pub_time_obj,
            )

            print('Parsed Result (ID: {}), created CBDPost (ID: {})'.format(
                result.id,
                post.id,
            ))
            mark_as_parsed(result)

        print('Complete')
