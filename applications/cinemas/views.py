from rest_framework.viewsets import ModelViewSet

from applications.cinemas.models import Cinema
from applications.cinemas.serializers import CinemaSerializer
from applications.movies.permissions import IsAdminOrReadOnly


class CinemaViewSet(ModelViewSet):
    serializer_class = CinemaSerializer
    queryset = Cinema.objects.all()
    permission_classes = (IsAdminOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
