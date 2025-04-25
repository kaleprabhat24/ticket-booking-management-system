# apps.py - Configuration for the core Django application

from django.apps import AppConfig

# CoreConfig defines settings for the 'core' app
class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Default field type for auto-incrementing primary keys
    name = 'core'                                          # Name of the app (should match folder name)
