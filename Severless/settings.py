"""
Django settings for Severless project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG","False").lower()=="true"

ALLOWED_HOSTS =os.environ.get("ALLOWED_HOSTS").split(" ") 
#['po4nwvbvwh.execute-api.us-east-1.amazonaws.com','127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
     "corsheaders",
     "django_extensions",
    "app_1",
    "zappa",
    "rest_framework",
    "django_cognito_jwt"
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
     "corsheaders.middleware.CorsMiddleware",
     "app_1.middleware.CognitoTokenMiddleware"
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
#REST_FRAMEWORK = {
#        'DEFAULT_AUTHENTICATION_CLASSES': [
#            'django_cognito_jwt.JSONWebTokenAuthentication',
#        ],
#     }
#from rest_framework_simplejwt.authentication import JWTAuthentication
#
#REST_FRAMEWORK = {
#    'DEFAULT_AUTHENTICATION_CLASSES': [
#        'app_1.authentication.CognitoJWTAuthentication',
#    ],
#}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
CORS_ALLOW_ALL_ORIGINS = True

#CORS_ORIGIN_ALLOW_ALL = True

#CORS_ALLOW_ALL_ORIGINS = False

COGNITO_USER_POOL_ID = 'us-east-1_LsUhND2zs'
COGNITO_APP_CLIENT_ID = '7g2af98fpbih3tgb28btf3vnkq'
COGNITO_AWS_REGION='us-east-1'
ROOT_URLCONF = "Severless.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Severless.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

#database_url=os.environ.get("DATABASE_URL")
#DATABASES["default"]=dj_database_url.parse(database_url)
#DATABASES = {
#    "default": {
#        "ENGINE": "django.db.backends.mysql",
#        "NAME": "Railway",
#        "USER": "root",
#        "PASSWORD": "bLBFspFztpTZi5fRoFyF",
#        "HOST": "containers-us-west-181.railway.app",
#        "PORT": "6976",
#        
#    }
#}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

#STATICFILES_DIRS = [
#    BASE_DIR / "static",
#]
# settings.py

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
