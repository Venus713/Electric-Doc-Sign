import os

def get_django_settings() -> str:
    return os.environ.get('DJANGO_SETTINGS_MODULE', 'config.settings.production')
