from django.core.management.base import BaseCommand

from scraper.models import Result


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Requesting site from CB...')
        cb_url = 'http://static.crunchbase.com/daily/content_share.html'
        result = Result.objects.from_url(cb_url)

        print('Response saved (ID {}).'.format(result.id))
