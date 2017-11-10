from .base import *  # noqa

DEBUG = True
SECRET_KEY = 'zxyzfv8by&)730=z&doua%c)arsb@4$w9wxp1amrorab!31cw_'

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cbdfeed',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}
