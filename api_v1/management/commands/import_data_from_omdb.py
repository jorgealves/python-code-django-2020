import uuid

from django.core.management import BaseCommand

from api_v1.models.episode import Episode
from api_v1.models.release import Release
from api_v1.services.omdb_api import OMDBApiService


class Command(BaseCommand):
    help = 'Created dynamodb tables'

    api = OMDBApiService

    def handle(self, *args, **options):
        try:
            self.import_title_data()
            self.import_episodes()
            self.stdout.write(self.style.SUCCESS('Command ran successfully.'))
        except Exception as ex:
            self.stdout.write(f'ERROR > {ex}', )

    def import_title_data(self) -> None:
        data = self.api.get_title_data()
        self.save_title_data(data=data)

    def import_episodes(self) -> None:
        seasons = self.api.get_total_seasons()
        for season_number in range(1, seasons+1):
            episodes = self.api.get_season_detail(season=season_number)
            for episode in episodes['Episodes']:
                detail = self.api.get_episode_detail(episode_id=episode['imdbID'])
                self.save_episode_detail(data=detail)

    def save_title_data(self, data: dict):
        new_release = Release()
        new_release.id = f'{uuid.uuid4()}'
        new_release.name = data['Title']
        new_release.year = data['Year']
        new_release.writer = data['Writer']
        new_release.plot = data['Plot']
        new_release.thumbnail = data['Poster']
        new_release.imdb_id = data['imdbID']
        new_release.imdb_rating = data['imdbRating']
        new_release.save()

    def save_episode_detail(self, data: dict):
        new_episode = Episode()
        new_episode.id = f'{uuid.uuid4()}'
        new_episode.title = data['Title']
        new_episode.episode_number = int(data['Episode'])
        new_episode.season = int(data['Season'])
        new_episode.series_imdb_id = data['seriesID']
        new_episode.release = data['Released']
        new_episode.thumbnail = data['Poster']
        new_episode.plot = data['Plot']
        new_episode.imdb_id = data['imdbID']
        new_episode.imdb_rating = data['imdbRating']
        new_episode.save()
