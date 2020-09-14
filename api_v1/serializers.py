import uuid

from rest_framework import serializers

from api.models.comment import Comment


class CommentSerializer(serializers.Serializer):
    episode_id = serializers.CharField()
    user_handler = serializers.CharField()
    comment = serializers.CharField()

    def create(self, validated_data):
        comment = Comment()
        comment.id = f'{uuid.uuid4()}'
        comment.episode_id = self.validated_data['episode_id']
        comment.user_handler = self.validated_data['user_handler']
        comment.comment = self.validated_data['comment']
        comment.save()
        return comment

    def update(self, instance, validated_data):
        instance.episode_id = self.validated_data['episode_id']
        instance.user_handler = self.validated_data['user_handler']
        instance.comment = self.validated_data['comment']
        instance.save()
