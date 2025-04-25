# settings.py - Configuration for Django project settings

import os
from pathlib import Path

# BASE_DIR defines the root directory for the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key for Django application (should be kept private in production)
SECRET_KEY = 'django-insecure-your-secret-key-here'

# Debug mode flag (should be False in production)
DEBUG = True

# ALLOWED_HOSTS defines which host/domain names your Django site can serve
ALLOWED_HOSTS = ['*']  # Allow all hosts during development

# List of installed apps for the project
INSTALLED_APPS = [
    'django.contrib.admin',       # Django's admin panel
    'django.contrib.auth',         # User authentication system
    'django.contrib.contenttypes', # Framework for content types
    'django.contrib.sessions',     # Session management
    'django.contrib.messages',     # Messaging framework
    'django.contrib.staticfiles',  # Static files handling
    'core',                        # The core application
]

# Middleware components for processing requests/responses
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Handles security-related tasks
    'django.contrib.sessions.middleware.SessionMiddleware',  # Manages session data
    'django.middleware.common.CommonMiddleware',  # Common request processing
    'django.middleware.csrf.CsrfViewMiddleware',  # Protects against CSRF attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Manages user authentication
    'django.contrib.messages.middleware.MessageMiddleware',  # Handles messages to users
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Prevents clickjacking
]

# Root URL configuration for the project
ROOT_URLCONF = 'ticket_booking.urls'

# Template configuration for rendering HTML files
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Template engine
        'DIRS': [],  # List of directories to search for templates (empty here)
        'APP_DIRS': True,  # Look for templates in app directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Provides debug context
                'django.template.context_processors.request',  # Provides request context
                'django.contrib.auth.context_processors.auth',  # User authentication context
                'django.contrib.messages.context_processors.messages',  # Message context
            ],
        },
    },
]

# WSGI application for handling web requests
WSGI_APPLICATION = 'ticket_booking.wsgi.application'

# Database configuration (using PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Using PostgreSQL
        'NAME': 'ticket_booking',                    # Database name
        'USER': 'admin',                             # Database user
        'PASSWORD': 'prabhat123',                    # Database password
        'HOST': 'db',                                # Database host (use 'db' in Docker setup)
        'PORT': '5432',                              # Default PostgreSQL port
    }
}

# Password validation settings for user authentication
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},  # Checks password similarity to user attributes
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},  # Ensures minimum password length
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},  # Prevents common passwords
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},  # Prevents passwords made of only digits
]

# Localization settings
LANGUAGE_CODE = 'en-us'  # Language setting for the project
TIME_ZONE = 'UTC'        # Time zone setting for the project
USE_I18N = True          # Enables internationalization
USE_TZ = True            # Enables timezone support

# Static files settings (for CSS, JS, images, etc.)
STATIC_URL = '/static/'  # URL to access static files
STATICFILES_DIRS = [BASE_DIR / "core/static"]  # Directory containing static files

# Default auto field type for primary keys (BigAutoField for large scale)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
