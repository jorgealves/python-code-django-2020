from django.conf import settings
from pynamodb.connection import TableConnection

original_init = TableConnection.__init__


def init(*args, **kwargs):
    kwargs['host'] = settings.DYNAMODB_HOST
    return original_init(*args, **kwargs)


TableConnection.__init__ = init
