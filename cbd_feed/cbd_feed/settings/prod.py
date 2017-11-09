import dj_database_url
import os

from .base import *  # noqa

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DATABASES = {
    'default': dj_database_url.parse(
        os.environ['DATABASE_URL'],
        conn_max_age=int(os.environ.get('DJANGO_DB_CONN_MAX_AGE', 0)),
    ),
}
