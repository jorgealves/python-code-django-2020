import random
import string
import uuid

import requests
from django.core.management import call_command
from rest_framework.test import APISimpleTestCase

from api_v1.models.episode import Episode


def string_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class TestViews(APISimpleTestCase):

    def setUp(self) -> None:
        call_command('refresh_dynamodb_tables')
        self.create_episode()

    def test_seasons_endpoint(self):
        result = self.client.get('/v1/seasons/')
        json = result.json()
        self.assertEquals(result.status_code, requests.codes.ok)
        self.assertIsInstance(json, dict)

    def test_seasons_detail_endpoint_success(self):
        result = self.client.get('/v1/seasons/1')
        json = result.json()
        self.assertEquals(result.status_code, requests.codes.ok)
        self.assertIsInstance(json, list)

    def test_seasons_detail_endpoint_404(self):
        result = self.client.get('/v1/seasons/asjdha')
        self.assertEquals(result.status_code, requests.codes.not_found)

    def test_episode_detail_endpoint(self):
        result = self.client.get('/v1/seasons/1/episode/1')
        json = result.json()
        self.assertEquals(result.status_code, requests.codes.ok)
        self.assertIsInstance(json, dict)

    def test_comment_endpoint(self):
        from api_v1.models.episode import Episode

        episodes = list(Episode.scan(Episode.season == 1))
        episode: Episode = next(filter(lambda x: x.episode_number == 1, episodes))
        header = {'Accept': 'application/json'}
        data = dict(
            episode_id=episode.id,
            user_handler='unittest.user.handler',
            comment='some unittest message'
        )

        result = self.client.post('/v1/seasons/1/episode/1/comment', headers=header, data=data)
        response = result.json()
        self.assertEquals(result.status_code, requests.codes.created)
        self.assertIsInstance(response, dict)

    def create_episode(self):
        new_episode = Episode()
        new_episode.id = f'{uuid.uuid4()}'
        new_episode.title = string_generator()
        new_episode.episode_number = 1
        new_episode.season = 1
        new_episode.series_imdb_id = string_generator()
        new_episode.release = string_generator()
        new_episode.thumbnail = string_generator()
        new_episode.plot = string_generator()
        new_episode.imdb_id = string_generator()
        new_episode.imdb_rating = string_generator()
        new_episode.save()
