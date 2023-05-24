from rest_framework import serializers

from applications.cinemas.models import Cinema
from applications.rooms.models import Room, Seat


class RoomSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Room
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['cinema'] = Cinema.objects.get(id=rep['cinema']).title
        return rep


class SeatSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Seat
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['room'] = Room.objects.get(id=rep['room']).title
        rep['cinema'] = Cinema.objects.get(id=rep['cinema']).title
        return rep

    def validate(self, attrs):
        row = attrs['row']
        place = attrs['place']
        room = Room.objects.filter(id=attrs['room'].id)[0]
        print(row)
        print(place)
        print(Seat.objects.filter(row=row, place=place, room=room.id))
        print('***********************************')

        if Seat.objects.filter(row=row, place=place, room=room.id):
            raise serializers.ValidationError('Это место уже забронировано')
        if room.rows < row:
            raise serializers.ValidationError('Количество рядов превышает возможное')
        if room.places < place:
            raise serializers.ValidationError('Количество мест превышает возможное')
        return attrs
