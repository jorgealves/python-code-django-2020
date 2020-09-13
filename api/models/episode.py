from pynamodb.attributes import UnicodeAttribute, NumberAttribute

from .base import IMDBMixin, BaseModel, ForeignKeyAttribute
from .release import Release


class Episode(BaseModel, IMDBMixin):
    title = UnicodeAttribute()
    episode_number = NumberAttribute()
    season = NumberAttribute()
    series_imdb_id = UnicodeAttribute()
    release = ForeignKeyAttribute(Release)
    thumbnail = UnicodeAttribute()
    plot = UnicodeAttribute()

    class Meta:
        table_name = 'episode'
