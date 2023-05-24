from rest_framework import serializers

from applications.cinemas.models import Cinema


class CinemaSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Cinema
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['owner'] = instance.owner.email
        return rep
