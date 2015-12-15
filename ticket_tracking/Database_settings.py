# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

import os

#Comment or delete line below if you don't want to use a SQLite DB.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
