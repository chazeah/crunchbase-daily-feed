from django.http import HttpResponse
from django.contrib.syndication.views import Feed
from content_parser.models import CBDPost


class LatestEntriesFeed(Feed):
    title = 'Crunchbase Daily'
    description = 'Feed containing data from the daily Crunchbase email.'
    link = '/feed/'

    def items(self):
        return CBDPost.objects.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body_content

    def item_pubdate(self, item):
        return item.published_at

    def item_link(self, item):
        post_id = 'https://cbd-feed.herokuapp.com/entry/{}'.format(item.id)
        return post_id
