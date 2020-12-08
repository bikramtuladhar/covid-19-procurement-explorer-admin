"""
Django settings for covidadmin project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import environ,os


environ.Env.read_env()
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
    CORS_ORIGIN_WHITELIST=(list, []),
    FETCH_COVID_DATA_INTERVAL=(int, 10800),
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env('ALLOWED_HOSTS')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'django_filters',
    'country',
    'vizualization',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.contrib.modeladmin',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtailvideos',
    'modelcluster',
    'taggit',
    'wagtail.api.v2',
    'content'
    # 'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'covidadmin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'covidadmin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST')
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATICFILES_DIRS = []
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = env('STATIC_URL')
FORCE_SCRIPT_NAME = env('FORCE_SCRIPT_NAME')

CORS_ORIGIN_WHITELIST = env('CORS_ORIGIN_WHITELIST')

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticatedOrReadOnly',),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
}


CELERY_BROKER_URL = env('CELERY_BROKER_URL')
CELERY_TIMEZONE = env('CELERY_TIMEZONE')
CELERY_TASK_ROUTES = {
    'country.tasks.fetch_covid_data': {
        'queue': 'covid19',
        'exchange': 'covid19',
        'routing_key': 'covid19'
        },
    'country.tasks.import_tender_data': {
        'queue': 'covid19',
        'exchange': 'covid19',
        'routing_key': 'covid19'
        },
    'country.tasks.local_currency_to_usd': {
        'queue': 'covid19',
        'exchange': 'covid19',
        'routing_key': 'covid19'
        },
}
CELERY_BEAT_SCHEDULE = {
    'fetch_covid_data_job': {
        'task': 'fetch_covid_data',  # the same goes in the task name
        'schedule': env('FETCH_COVID_DATA_INTERVAL'),  # 3*60*60,  # in seconds
        'options': {
            'queue': 'covid19',
            'exchange': 'covid19',
            'routing_key': 'covid19'
            },
    },
}

GOOGLE_SHEET_CREDENTIALS_JSON = env('GOOGLE_SHEET_CREDENTIALS_JSON')
FIXER_IO_API_KEY = env('FIXER_IO_API_KEY')

WAGTAIL_SITE_NAME = 'Covid procurement admin'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = env('MEDIA_URL')
MAX_UPLOAD_SIZE = "104857600"  # 100 MB
