from django.contrib.auth import get_user_model
from rest_framework import serializers

from applications.cinemas.models import Cinema
from applications.movies.models import Movie
from applications.rooms.models import Room
from applications.tickets.models import Ticket

User = get_user_model()


class TicketSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.email')

    cost = {
        'children': 150,
        'student': 200,
        'adult': 250,
    }

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

    def validate(self, attrs):
        ticket_type = attrs['ticket_type']
        user = User.objects.get(id=attrs['owner'].id)
        if user.card_balance < self.cost[ticket_type]:
            raise serializers.ValidationError('В вашем балансе недостаточно средств')
        return attrs

    def create(self, validated_data):
        user = User.objects.get(id=validated_data['owner'].id)
        user.card_balance -= self.cost[validated_data['ticket_type']]
        user.save()
        ticket = Ticket.objects.create(**validated_data)
        return ticket
