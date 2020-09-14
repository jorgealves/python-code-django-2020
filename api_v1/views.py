import requests
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from api_v1.models.comment import Comment
from api_v1.models.episode import Episode
from api_v1.models.release import Release
from api_v1.serializers import CommentSerializer


class ListTitleView(APIView):
    """Main endpoint to get Game Of Thrones title info"""
    http_method_names = ['get']

    def get_object(self):
        return Release.scan()

    def get(self, request, *args, **kwargs):
        obj: Release = next(self.get_object())
        result = {
            'id': obj.id,
            'name': obj.name,
            'thumbnail': obj.thumbnail,
            'imdb_rating': obj.imdb_rating,
            'writer': obj.writer,
            'plot': obj.plot
        }
        return Response(data=result, status=requests.codes.ok)


class ListSeasonsView(APIView):
    """List all seasons links"""
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        result = dict()
        for number in range(1, 9):
            result[number] = reverse('get-season', args=(number,))
        return Response(result, status=requests.codes.ok)


class EpisodesListView(ListAPIView):
    """List all episodes by a given season ID"""
    http_method_names = ['get']

    def get_queryset(self):
        pass

    def get(self, request, *args, **kwargs):
        season_number = kwargs['id']
        if not season_number:
            return Response(status=requests.codes.not_found)

        episodes = Episode.scan(Episode.season == season_number)

        result = []
        for row in list(episodes):
            result.append({
                'title': row.title,
                'episode_number': row.episode_number,
                'season': row.season,
                'series_imdb_id': row.series_imdb_id,
                'release': row.release,
                'thumbnail': row.thumbnail,
                'plot': row.plot,
                'imdb_rating': row.imdb_rating,
                'imdb_id': row.imdb_id,
            })

        result.sort(key=lambda x: x['episode_number'])
        return Response(data=result, status=requests.codes.ok)


class EpisodesDetailView(ListAPIView):
    """List Episode detail with all comments"""
    http_method_names = ['get']
    season = None
    episode = None

    def get_object(self):
        return list(Episode.scan(Episode.season == self.season))

    def get(self, request, *args, **kwargs):
        self.season = kwargs['season']
        self.episode = kwargs['episode']
        if not self.season:
            return Response(status=requests.codes.not_found)
        if not self.episode:
            return Response(status=requests.codes.not_found)

        episode: Episode = next(filter(lambda x: x.episode_number == self.episode, self.get_object()))
        comment_list = list(Comment.scan(Comment.episode_id == episode.id))
        comment_result = [
            {
                'user': row.user_handler,
                'comment': row.comment
            } for row in comment_list
        ]
        result = {
            'id': episode.id,
            'title': episode.title,
            'episode_number': episode.episode_number,
            'season': episode.season,
            'series_imdb_id': episode.series_imdb_id,
            'release': episode.release,
            'thumbnail': episode.thumbnail,
            'plot': episode.plot,
            'imdb_rating': episode.imdb_rating,
            'imdb_id': episode.imdb_id,
            'comments': comment_result
        }

        return Response(data=result, status=requests.codes.ok)


class CommentView(ListCreateAPIView):
    """Post a comment to a episode"""
    http_method_names = ['post', 'delete']
    serializer_class = CommentSerializer
