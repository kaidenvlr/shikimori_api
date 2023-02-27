from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    date_added = models.DateTimeField(auto_now=True, verbose_name='Дата добавления в базу')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class AgeRating(models.Model):
    title = models.CharField(max_length=10, verbose_name='Название')
    description = models.CharField(max_length=400, verbose_name='Описание')
    date_added = models.DateTimeField(auto_now=True, verbose_name='Дата добавления в базу')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Возрастной рейтинг'
        verbose_name_plural = 'Возрастные рейтинги'


class Studio(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    date_added = models.DateTimeField(auto_now=True, verbose_name='Дата добавления в базу')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Студия'
        verbose_name_plural = 'Студии'


class Status(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    date_added = models.DateTimeField(auto_now=True, verbose_name='Дата добавления в базу')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class AnimeType(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    date_added = models.DateTimeField(auto_now=True, verbose_name='Дата добавления в базу')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Anime(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=500, verbose_name='Описание')
    qty_episodes = models.PositiveSmallIntegerField(verbose_name='Количество эпизодов')
    len_episode = models.PositiveSmallIntegerField(verbose_name='Длительность эпизода', help_text='Указывать в минутах')
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, verbose_name='Студия')
    type = models.ForeignKey(AnimeType, on_delete=models.CASCADE, verbose_name='Тип')
    genre = models.ManyToManyField(Genre, verbose_name='Жанры')
    poster = models.ImageField(verbose_name='Постер', upload_to='poster/')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус')
    release_year = models.PositiveSmallIntegerField(verbose_name='Год выпуска', default=0)
    date_added = models.DateTimeField(auto_now=True, verbose_name='Дата добавления в базу')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'
