"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""








'''
============================================
============================================
SUPERUSER:

usermane: admin
email: admin@mail.com
PW: 123456



STANDARD TEST USER:

User1
User2
User3
User40
User50
User60

All Test user PWs - Password!.0
============================================
============================================
'''








'''
============================================
============================================
URL'S -

HOME:
http://localhost:8000/

INVENTORY:
http://localhost:8000/inventory/
http://localhost:8000/inventory/new
http://localhost:8000/inventory/37/edit


CALENDAR:
http://localhost:8000/calendar/
http://localhost:8000/calendar/booking/edit/65/

FINANCE:
http://localhost:8000/finance/

LOGOUT:
http://localhost:8000/login/logout/

LOGIN:
http://localhost:8000/login/    - NO RESTRICTED ACCESS, NEED TO ACCES TO LOGIN

PAYMENTS:
http://localhost:8000/payment/  - NO RESTRICTED ACCESS, NEED TO ACCES TO LOGIN


REGISTER:
http://localhost:8000/login/register/   -   NO RESTRICTED ACCESS, NEED TO ACCES TO LOGIN, NOTHING TO STOP YOU GOING HERE WITHOUT PAYING

============================================
============================================
'''




from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=pzg$lhwwp3yej_3#@imho4mzyc0!y5skk&dw-ox-1vku9aha)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'inventory_component',
    'login_register_component',
    'calendar_component',
    'finance_component',
    'payment_component',
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

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'static/templates'
        ],
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

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




LOGIN_REDIRECT_URL = '/'



# Stripe Keys
STRIPE_PUBLIC_KEY = os.environ.get('pk_test_51MaePkDhcRijS6ewfmHiSeujJ3r8bCmKd8rjwuGecW78lkQD30KOgIrXLGlewjhpzKQxYCtDUdWZPUV3VfEbsBLr00NlgMxUBv')
STRIPE_SECRET_KEY = os.environ.get('sk_test_51MaePkDhcRijS6ew9XYy463jjZbdyHiuNnGbQzrTzB7F5GaCSFVbGarnYjoTk5e0A5KCQjr2QDgqrV3LZELovzz3001mHNrZ7X')