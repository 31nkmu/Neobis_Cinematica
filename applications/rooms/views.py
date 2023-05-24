from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from applications.movies.permissions import IsAdminOrReadOnly
from applications.rooms.models import Room, Seat
from applications.rooms.serializers import RoomSerializer, SeatSerializer


class RoomViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = (IsAdminOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SeatViewSet(ModelViewSet):
    serializer_class = SeatSerializer
    queryset = Seat.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
