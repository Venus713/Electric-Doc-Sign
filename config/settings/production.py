from .stage import *


ENV_NAME = os.environ.get('ENV_NAME', "production")
STATICFILES_LOCATION = '%s/static' % ENV_NAME
MEDIAFILES_LOCATION = '%s/media' % ENV_NAME

DATABASES['default'] = dj_database_url.config(
    default='postgres://{user}:{password}@{host}:{port}/{db}'.format(
        user=os.environ.get('DB_USERNAME'),
        password=os.environ.get('DB_PASSWORD'),
        host=os.environ.get('DB_HOST'),
        port=os.environ.get('DB_PORT'),
        db=os.environ.get('DB_NAME'),
    )
)
