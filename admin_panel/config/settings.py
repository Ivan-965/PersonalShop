from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = BASE_DIR.parent
load_dotenv(PROJECT_ROOT / '.env')

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'store'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}

JAZZMIN_SETTINGS = {
    'site_title': 'Storx',
    'site_header': 'Panel of store',
    'site_brand': 'Store_brand',
    'welcome': 'Welcome',
    'custom_css': 'css/custom_admin.css',

    'search_model': ['store.Users', 'store.Products', 'store.Categories'],
    'copyright': 'Store',

    'topmenu_links': [{
        'name': 'Главная',
        'url': 'admin:index'
    },
        {'name': 'ТГ-бот магазина',
         'url': 'https://t.me/P_shop404Bot',
         'new_window': True,
         }, ],
    'icons': {'store.Users': 'fas fa-User',
              'store.Products': 'fas fa-cookie',
              'store.Orders': 'fas fa-tag', },
    'show_sidebar': True,
    'navigation_expanded': True,
    'hide_apps': [],

    'order_with_respect_to': ['store', 'auth']

}

JAZZMIN_UI_TWEAKS = {
    'theme': 'sketchy',
    'navbar_small_text': True,
    'footer_small_text': True,
    'body_small_text': True,
    'brand_color': 'navbar-dark-primary',
    'accent': 'accent-warning',

    'navbar': 'navbar-dark navbar-primary navbar-shadow',
    'no_navbar_border': True,
    'sidebar': 'sidebar-dark-primary',
    'sidebar_nav_small_text': True,
}