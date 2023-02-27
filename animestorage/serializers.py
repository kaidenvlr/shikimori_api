from rest_framework import serializers

from animestorage.models import Genre, Studio, Status, AnimeType, Anime, AgeRating


class GenreSerializer(serializers.Serializer):
    class Meta:
        model = Genre
        fields = ['id', 'title', 'description', 'date_added']


class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = ['id', 'title', 'date_added']


class AgeRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeRating
        fields = ['id', 'title', 'description', 'date_added']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'title', 'date_added']


class AnimeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeType
        fields = ['id', 'title', 'date_added']


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['id', 'title', 'description', 'qty_episodes',
                  'len_episode', 'studio', 'type', 'genre',
                  'poster', 'status', 'release_year', 'date_added']
