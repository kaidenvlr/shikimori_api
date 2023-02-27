from rest_framework import generics

from animestorage import models
from animestorage import serializers
from animestorage.permissions import IsAdminOrReadOnly


# anime
class AnimeAPIListCreate(generics.ListCreateAPIView):
    queryset = models.Anime.objects.all()
    serializer_class = serializers.AnimeSerializer
    permission_classes = (IsAdminOrReadOnly,)


class AnimeAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Anime.objects.all()
    serializer_class = serializers.AnimeSerializer
    permission_classes = (IsAdminOrReadOnly,)


# anime type
class AnimeTypeAPIListCreate(generics.ListCreateAPIView):
    queryset = models.AnimeType.objects.all()
    serializer_class = serializers.AnimeTypeSerializer
    permission_classes = (IsAdminOrReadOnly,)


class AnimeTypeAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AnimeType.objects.all()
    serializer_class = serializers.AnimeTypeSerializer
    permission_classes = (IsAdminOrReadOnly,)


class StatusAPIListCreate(generics.ListCreateAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    permission_classes = (IsAdminOrReadOnly,)


class StatusAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    permission_classes = (IsAdminOrReadOnly,)


class GenreAPIListCreate(generics.ListCreateAPIView):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)


class GenreAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)


class AgeRatingAPIListCreate(generics.ListCreateAPIView):
    queryset = models.AgeRating.objects.all()
    serializer_class = serializers.AgeRatingSerializer
    permission_classes = (IsAdminOrReadOnly,)


class AgeRatingAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AgeRating.objects.all()
    serializer_class = serializers.AgeRatingSerializer
    permission_classes = (IsAdminOrReadOnly,)


class StudioAPIListCreate(generics.ListCreateAPIView):
    queryset = models.Studio.objects.all()
    serializer_class = serializers.StudioSerializer
    permission_classes = (IsAdminOrReadOnly,)


class StudioAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Studio.objects.all()
    serializer_class = serializers.StudioSerializer
    permission_classes = (IsAdminOrReadOnly,)
