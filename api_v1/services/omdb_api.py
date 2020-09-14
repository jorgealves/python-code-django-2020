import requests
from django.conf import settings
from requests import Response


class OMDBApiService:
    base_url = settings.OMDBAPI_URL
    title_url = f'{base_url}&t=Game%20Of%20Thrones&plot=full'
    base_query_url = f'{base_url}&plot=full'
    seasons_parameter_pattern = '&Season='
    episode_parameter_pattern = '&i='

    headers = {
        'Accept': 'application/json'
    }

    @classmethod
    def _get_parsed_response(cls, response: Response) -> dict:
        return response.json()

    @classmethod
    def get_title_data(cls):
        return cls._get_parsed_response(requests.get(
            url=f'{cls.title_url}',
            headers=cls.headers
        ))

    @classmethod
    def get_total_seasons(cls) -> int:
        return int(cls.get_title_data()['totalSeasons'])

    @classmethod
    def get_season_detail(cls, season: int) -> dict:
        return cls._get_parsed_response(requests.get(
            url=f'{cls.title_url}{cls.seasons_parameter_pattern}{season}',
            headers=cls.headers
        ))

    @classmethod
    def get_episode_detail(cls, episode_id: str) -> dict:
        return cls._get_parsed_response(requests.get(
            url=f'{cls.base_query_url}{cls.episode_parameter_pattern}{episode_id}',
            headers=cls.headers
        ))
