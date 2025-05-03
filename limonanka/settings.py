import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = BASE_DIR / '.env'
load_dotenv(dotenv_path=dotenv_path)

SECRET_KEY = os.environ.get('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')
CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS', 'localhost').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'django_ckeditor_5',


    'apps.about.apps.AboutConfig',
    'apps.blogs.apps.BlogsConfig',
    'apps.brands.apps.BrandsConfig',
    'apps.contact.apps.ContactConfig',
    'apps.faqs.apps.FaqsConfig',
    'apps.features.apps.FeaturesConfig',
    'apps.gallery.apps.GalleryConfig',
    'apps.homepage.apps.HomepageConfig',
    'apps.products.apps.ProductsConfig',
    'apps.referances.apps.ReferancesConfig',
    'apps.services.apps.ServicesConfig',
    'apps.sliders.apps.SlidersConfig',
    'apps.stats.apps.StatsConfig',
    'apps.testimonials.apps.TestimonialsConfig',
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

ROOT_URLCONF = 'limonanka.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.contact.context_processors.contact_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'limonanka.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'tr'
TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

###(static_url staticfiles olabilir ?)
STATIC_URL = '/staticfiles/' 
STATICFILES_DIRS = [  BASE_DIR / 'static',  ]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_ROOT = os.getenv('STATIC_ROOT') or BASE_DIR / 'staticfiles'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CKEDITOR_5_CUSTOM_CSS = 'fix.css'



# CKEditor 5 Configs
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
        'config': {
            'language': 'tr',
        },
    },
    'extends': {
        'blockToolbar': [
            'heading', '|',
            'blockQuote', 'imageUpload'
        ],
        'toolbar': [
            'heading', '|',
            'bold', 'italic', 'underline', 'strikethrough', 'subscript', 'superscript', '|',
            'link', 'bulletedList', 'numberedList', 'todoList', '|',
            'blockQuote', 'insertTable', 'mediaEmbed', '|',
            'alignment', '|',
            'fontColor', 'fontBackgroundColor', '|',
            'highlight', '|',
            'horizontalLine', '|',
            'removeFormat', '|',
            'specialCharacters', '|',
            'sourceEditing'
        ],
        'heading': {
            'options': [
                { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
                { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
                { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' },
                { 'model': 'heading4', 'view': 'h4', 'title': 'Heading 4', 'class': 'ck-heading_heading4' },
                { 'model': 'heading5', 'view': 'h5', 'title': 'Heading 5', 'class': 'ck-heading_heading5' },
                { 'model': 'heading6', 'view': 'h6', 'title': 'Heading 6', 'class': 'ck-heading_heading6' }
            ]
        },
        'image': {
            'toolbar': [
                'imageTextAlternative', 'imageStyle:full', 'imageStyle:side', '|',
                'linkImage'
            ]
        },
        'table': {
            'contentToolbar': [
                'tableColumn', 'tableRow', 'mergeTableCells', '|',
                'tableCellProperties', 'tableProperties'
            ]
        },
        'mediaEmbed': {
            'previewsInData': True
        },
        'height': 300,
        'width': '100%',
        'config': {
            'language': 'tr',
        },
    }
}