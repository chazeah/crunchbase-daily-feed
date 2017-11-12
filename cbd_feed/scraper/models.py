import requests

from django.db import models


class ResultManager(models.Manager):
    def from_url(self, url):
        result = requests.get(url)
        result = self.create(
            response_code=result.status_code,
            response_text=result.text,
            url=url,
        )
        return result


class Result(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    has_been_parsed = models.BooleanField(default=False)
    parsed_at = models.DateTimeField(blank=True, null=True)
    response_code = models.PositiveIntegerField()
    response_text = models.TextField()
    url = models.URLField()

    objects = ResultManager()

    class Meta:
        ordering = ('created_at', )

    def __str__(self):
        return 'Requested on {}'.format(self.created_at)
