from _include.Chimera.Chimera.databases import databases
import sys
import os


git_submodules = [
    '_include/Chimera/',
]

for directory in git_submodules:
    path = os.path.join(directory)
    if path not in sys.path:
        sys.path.append(path)

PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Michael', 'michael@mealsloth.com'),
)

MANAGERS = ADMINS

DATABASES = databases()

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'admin.mealsloth.com']

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = '/login/'

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'wi=od%+rgt^bdabhp3qdq)b!xb0+_q2^faa$dkh65wja-%j&n+'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Valkyrie.urls'

WSGI_APPLICATION = 'Valkyrie.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Valkyrie',
    'Chimera',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'Valkyrie.gae_memcached_cache.GaeMemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

# For testing authentication
AUTH_TEST_USER_USERNAME = 'authtestuser'
AUTH_TEST_USER_PASSWORD = 's5dfBekmGW48KfNxb7q8Je2N'
