from rest_framework import generics
from events.models import Event
from events.serializers import EventSerializer
from startups.permissions import IsAdminOrReadOnly


class EventsAPIList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAdminOrReadOnly,)


class EventsAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAdminOrReadOnly,)