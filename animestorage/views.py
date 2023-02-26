from rest_framework import generics

from animestorage import models
from animestorage import serializers
from animestorage.permissions import IsAdminOrReadOnly


class AnimeAPIList(generics.ListCreateAPIView):
    queryset = models.Anime.objects.all()
    serializer_class = serializers.AnimeSerializer


class AnimeAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Anime.objects.all()
    serializer_class = serializers.AnimeSerializer
    permission_classes = (IsAdminOrReadOnly,)
