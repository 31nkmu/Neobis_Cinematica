from rest_framework.viewsets import ModelViewSet

from applications.feedback.mixins import FavoriteMixin, CommentMixin, RatingMixin, LikeMixin
from applications.movies.models import Movie
from applications.movies.permissions import IsAdminOrReadOnly
from applications.movies.serializers import MovieSerializer


class MovieViewSet(ModelViewSet, FavoriteMixin, CommentMixin, RatingMixin, LikeMixin):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = (IsAdminOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
