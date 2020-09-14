from pynamodb.attributes import UnicodeAttribute

from .base import BaseModel


class Comment(BaseModel):
    episode_id = UnicodeAttribute(null=False)
    user_handler = UnicodeAttribute(null=False)
    comment = UnicodeAttribute(null=False)

    class Meta:
        table_name = 'comment'
