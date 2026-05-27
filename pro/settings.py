from pathlib import Path


# =========================
# BASE DIRECTORY
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent



# =========================
# SECURITY
# =========================

SECRET_KEY = 'secret-key'

DEBUG = True

ALLOWED_HOSTS = []



# =========================
# INSTALLED APPS
# =========================

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'app',

]



# =========================
# MIDDLEWARE
# =========================

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]



# =========================
# ROOT URLS
# =========================

ROOT_URLCONF = 'pro.urls'



# =========================
# TEMPLATES
# =========================

TEMPLATES = [

    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [BASE_DIR / 'templates'],

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



# =========================
# WSGI
# =========================

WSGI_APPLICATION = 'pro.wsgi.application'



# =========================
# DATABASE
# =========================

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE_DIR / 'db.sqlite3',

    }

}



# =========================
# PASSWORD VALIDATION
# =========================

AUTH_PASSWORD_VALIDATORS = []



# =========================
# LANGUAGE & TIMEZONE
# =========================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True



# =========================
# STATIC FILES
# =========================

STATIC_URL = 'static/'

STATICFILES_DIRS = [

    BASE_DIR / 'pro/static'

]



# =========================
# MEDIA FILES
# =========================

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'pro/media'



# =========================
# DEFAULT AUTO FIELD
# =========================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'