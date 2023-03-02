from django.db import models


class AnimeWatchStatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Статус аниме у пользователя'
        verbose_name_plural = 'Статусы аниме у пользователя'

    def __str__(self):
        return self.name
