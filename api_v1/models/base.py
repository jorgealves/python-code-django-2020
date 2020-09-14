import uuid
from datetime import datetime

from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute, NumberAttribute
from pynamodb.constants import PAY_PER_REQUEST_BILLING_MODE
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
from pynamodb.models import Model

from django.conf import settings


class BaseModel(Model):
    """Base DynamoDB model"""
    id = UnicodeAttribute(hash_key=True, default=f'{uuid.uuid4()}')
    created = UTCDateTimeAttribute(default=datetime.utcnow())

    class Meta:
        region = settings.REGION
        billing_mode = PAY_PER_REQUEST_BILLING_MODE
        if settings.DYNAMODB_HOST is not None:
            host = settings.DYNAMODB_HOST


class BaseGSI(GlobalSecondaryIndex):
    class Meta:
        billing_mode = PAY_PER_REQUEST_BILLING_MODE
        projection = AllProjection()
        # read_capacity_units = 5
        # write_capacity_units = 5


class ForeignKeyAttribute(UnicodeAttribute):

    def __init__(self, model, **kwargs):
        self.is_foreign_key = True
        self.foreign_model = model
        super().__init__(**kwargs)


class IMDBMixin:
    imdb_rating = UnicodeAttribute()
    imdb_id = UnicodeAttribute()
