from django.contrib import admin

from animestorage.models import Studio, Genre, Status, AnimeType, AgeRating, Anime


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    readonly_fields = ['id', 'date_added']


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    readonly_fields = ['id', 'date_added']


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    readonly_fields = ['id', 'date_added']


@admin.register(AnimeType)
class AnimeTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    readonly_fields = ['id', 'date_added']


@admin.register(AgeRating)
class AgeRatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    readonly_fields = ['id', 'date_added']


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'poster', 'title', 'qty_episodes', 'len_episode']
    readonly_fields = ['id', 'date_added']
