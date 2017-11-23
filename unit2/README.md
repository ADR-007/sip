# Django RESTful API Angular Skeleton 

### Commands
1. Run server: `make run`
2. Make migrations: `make make`.
3. Migrate DB: `make migrate`.
4. Reset local server: `make port`.
5. Create superuser root root: `make super`.


### Local settings

```
import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    }
}

DEBUG = True

MEDIA_ROOT = os.path.normpath(os.path.join(SITE_ROOT, "./media"))
STATIC_ROOT = os.path.normpath(os.path.join(SITE_ROOT, "./static"))

```

### Secret Keys

```
SECRET_KEY = "SECRET_KEY"

```