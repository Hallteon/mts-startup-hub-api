from rest_framework import generics
from events.models import Event
from events.serializers import EventSerializer, EventCertainSerializer
from startups.permissions import IsAdminOrReadOnly


class EventsAPIList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventsAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventsCertainAPIList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCertainSerializer
