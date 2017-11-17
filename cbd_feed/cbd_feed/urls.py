from django.conf.urls import (
    include,
    url,
)
from django.contrib import admin


urlpatterns = [
    url(r'^feed/', include('feed_gen.urls')),
    url(r'^admin/', admin.site.urls),
]
