from pynamodb.attributes import UnicodeAttribute

from .base import BaseModel, ForeignKeyAttribute
from .episode import Episode


class Comment(BaseModel):
    episode = ForeignKeyAttribute(Episode)
    user_handler = UnicodeAttribute()
    comment = UnicodeAttribute()

    class Meta:
        table_name = 'comment'
