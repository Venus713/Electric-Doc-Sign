from .base import *

ENV_NAME = os.environ.get('ENV_NAME', "local")
STATICFILES_LOCATION = '%s/static' % ENV_NAME
MEDIAFILES_LOCATION = '%s/media' % ENV_NAME
