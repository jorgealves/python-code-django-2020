from pynamodb.attributes import UnicodeAttribute, NumberAttribute

from .base import IMDBMixin, BaseModel, ForeignKeyAttribute, BaseGSI
from .release import Release


class TitleSeasonEpisodeIndex(BaseGSI):
    title = UnicodeAttribute()
    season = NumberAttribute(hash_key=True)
    episode = NumberAttribute(range_key=True)


class Episode(BaseModel, IMDBMixin):
    # title_season_episode_index = TitleSeasonEpisodeIndex()

    title = UnicodeAttribute()
    episode_number = NumberAttribute()
    season = NumberAttribute()
    series_imdb_id = UnicodeAttribute()
    release = ForeignKeyAttribute(Release)
    thumbnail = UnicodeAttribute()
    plot = UnicodeAttribute()

    class Meta:
        table_name = 'episode'
