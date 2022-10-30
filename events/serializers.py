from rest_framework import serializers
from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventCertainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('platform', 'description', 'theme', 'date', 'time')
