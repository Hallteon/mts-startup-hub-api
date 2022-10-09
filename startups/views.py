from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from startups.models import Startup, Stage, Program
from startups.permissions import IsOwner, IsAdminOrReadOnly
from startups.serializers import StartupSerializer, ProgramSerializer, StageSerializer


class StartupsAPIList(generics.ListCreateAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    permission_classes = (IsAuthenticated,)


class ProgramStartupsAPIList(generics.ListAPIView):
    serializer_class = StartupSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        startups = Startup.objects.filter(program__pk=self.kwargs['pk'])

        return startups


class StageStartupsAPIList(generics.ListAPIView):
    serializer_class = StartupSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        startups = Startup.objects.filter(stage__pk=self.kwargs['pk'])

        return startups


class StartupsAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class ProgramsAPIList(generics.ListCreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ProgramsAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = (IsAdminOrReadOnly,)


class StagesAPIList(generics.ListCreateAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
    permission_classes = (IsAdminOrReadOnly,)


class StagesAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
    permission_classes = (IsAdminOrReadOnly,)