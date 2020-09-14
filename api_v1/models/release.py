from pynamodb.attributes import UnicodeAttribute

from api_v1.models.base import BaseModel, IMDBMixin


class Release(BaseModel, IMDBMixin):
    """This model represent any kind of release (Music, book, movie, tv show, etc)"""

    name = UnicodeAttribute(null=False)
    year = UnicodeAttribute(null=False)
    writer = UnicodeAttribute(null=False)
    plot = UnicodeAttribute(null=False)
    thumbnail = UnicodeAttribute(null=False)

    class Meta:
        table_name = 'release'
