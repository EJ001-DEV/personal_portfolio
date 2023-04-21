"""
Django settings for django_portfolio project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
import environ  # <-- Updated!
from decouple import config
#from dotenv import load_dotenv

#load_dotenv('.env')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(BASE_DIR / '.env')  # <-- Updated!

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')
#SECRET_KEY = env('SECRET_KEY')  # <-- Updated!

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = 'RENDER' not in os.environ

DEBUG = os.environ.get('DEBUG')

env = environ.Env(  # <-- Updated!
    # set casting, default value
    DEBUG=(bool, False),    
)

'''
ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:    
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
'''

#ALLOWED_HOSTS = ['.vercel.app', '.now.sh']
#ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']
ALLOWED_HOSTS = ['.vercel.app','127.0.0.1'] # Allow *.vercel.app

#CSRF_TRUSTED_ORIGINS = ['https://*.fly.dev']  # <-- Updated!





# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    #'whitenoise.runserver_nostatic',  # <-- Updated!
    'django.contrib.staticfiles',
    'blog',
    'portfolio',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    #'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',    
]

ROOT_URLCONF = 'django_portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_portfolio.wsgi.application'
#WSGI_APPLICATION = 'django_portfolio.wsgi.app'
#WSGI_APPLICATION = 'vercel_app.wsgi.app'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

#DATABASES['default'] = dj_database_url.config()
DATABASES = {
'default': dj_database_url.config(     
        default='postgres://EJ001-DEV:5CZ0EGeBOkKx@ep-soft-sky-263817.us-east-2.aws.neon.tech/neondb',        
        conn_max_age=600    
        )
} 


'''
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'URL': os.getenv('POSTGRES_URL'),
    'NAME': os.getenv('PGNAME'),
    'USER': os.getenv('PGUSER'),
    'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
    'HOST': os.getenv('PGHOST'),
    'PORT': os.getenv('PGPORT'),
    }
}
'''



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

#STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles_build' / 'static/'
#STATIC_ROOT = BASE_DIR / 'static/'
#STATICFILES_DIRS = [BASE_DIR / 'static/',]
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

#STATIC_URL = 'static/'
#MEDIA_URL = '/media/'
#MEDIA_ROOT = BASE_DIR / 'mediafiles_build' / 'media'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#MEDIA_URL = '/media/'
#MEDIA_ROOT = BASE_DIR / 'uploads'

#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATIC_ROOT = BASE_DIR / 'static/'

#print('STATIC_ROOT: ' + str(STATIC_ROOT))

#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



#STATIC_ROOT = BASE_DIR / "static"
#STATIC_ROOT = BASE_DIR / 'staticfiles_build' / "static"





# Following settings only make sense on production and may break development environments.
#if not DEBUG:    # Tell Django to copy statics to the `staticfiles` directory
    # in your application directory on Render.
    #STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#MEDIA_ROOT = BASE_DIR / 'media'

#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')




#TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates/'),)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
