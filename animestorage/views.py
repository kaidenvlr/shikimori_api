from rest_framework import generics

from animestorage import models
from animestorage import serializers
from animestorage.permissions import IsAdminOrReadOnly


# anime
class AnimeAPIList(generics.ListCreateAPIView):
    queryset = models.Anime.objects.all()
    serializer_class = serializers.AnimeSerializer
    permission_classes = (IsAdminOrReadOnly,)


class AnimeAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Anime.objects.all()
    serializer_class = serializers.AnimeSerializer
    permission_classes = (IsAdminOrReadOnly,)


# anime type
class AnimeTypeAPIList(generics.ListCreateAPIView):
    queryset = models.AnimeType.objects.all()
    serializer_class = serializers.AnimeTypeSerializer
    permission_classes = (IsAdminOrReadOnly,)


class AnimeTypeAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AnimeType.objects.all()
    serializer_class = serializers.AnimeTypeSerializer
    permission_classes = (IsAdminOrReadOnly,)
