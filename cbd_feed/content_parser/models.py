from django.db import models


class CBDPost(models.Model):
    body_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField()
    title = models.TextField()

    class Meta:
        ordering = ('published_at', )
        verbose_name = 'CBD Post'
        verbose_name_plural = 'CBD Posts'

    def __str__(self):
        return 'Post from {}'.format(self.published_at)
