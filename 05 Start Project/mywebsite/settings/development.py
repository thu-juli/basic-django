from .base import *


DEBUG = True

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Override Installed Apps
INSTALLED_APPS += [

]
