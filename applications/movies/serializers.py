from django.db.models import Avg
from rest_framework import serializers

from applications.cinemas.models import Cinema
from applications.feedback.models import Like, Rating, Comment
from applications.feedback.serializers import CommentSerializer
from applications.feedback.services import is_fan, is_reviewer, is_commented, is_favorite
from applications.movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Movie
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        user = self.context.get('request').user
        rep['likes'] = Like.objects.filter(movie=instance, like=True).count()
        rating = Rating.objects.filter(movie=instance).aggregate(Avg('rating'))['rating__avg']
        if rating:
            rep['rating'] = rating
        else:
            rep['rating'] = 0
        comments = Comment.objects.filter(movie=instance)
        comments = CommentSerializer(comments, many=True).data
        comments = [{'user': i['user'], 'comment': i['comment']} for i in comments]
        rep['comments'] = comments
        rep['is_fan'] = is_fan(user=user, obj=instance)
        rep['is_reviewer'] = is_reviewer(user=user, obj=instance)
        rep['is_commented'] = is_commented(user=user, obj=instance)
        rep['is_favorite'] = is_favorite(user=user, obj=instance)
        rep['cinema'] = Cinema.objects.get(id=rep['cinema']).title
        return rep
