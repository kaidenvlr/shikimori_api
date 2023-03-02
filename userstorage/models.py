from django.db import models
from django.contrib.auth.models import User
from animestorage.models import Anime


class AnimeWatchStatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Статус аниме у пользователя'
        verbose_name_plural = 'Статусы аниме у пользователя'

    def __str__(self):
        return self.name


class ProfileListAnime(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    status = models.ForeignKey(AnimeWatchStatus, on_delete=models.CASCADE, verbose_name='Статус')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, verbose_name='Аниме')
    qty_episodes = models.PositiveSmallIntegerField(verbose_name='Количество просмотренных эпизодов')

    class Meta:
        verbose_name = 'Аниме у пользователя'
        verbose_name_plural = 'Аниме у пользователей'

    def __str__(self):
        return f"{self.user.username} - {self.anime.title}"
