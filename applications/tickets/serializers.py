from django.contrib.auth import get_user_model
from rest_framework import serializers

from applications.cinemas.models import Cinema
from applications.movies.models import Movie
from applications.rooms.models import Room
from applications.tickets.models import Ticket

User = get_user_model()


class TicketSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Ticket
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['room'] = Room.objects.get(id=rep['room']).title
        rep['cinema'] = Cinema.objects.get(id=rep['cinema']).title
        rep['owner'] = User.objects.get(id=rep['owner']).email
        rep['movie'] = Movie.objects.get(id=rep['movie']).title
        return rep
