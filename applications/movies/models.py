from django.contrib.auth import get_user_model
from django.db import models

from applications.cinemas.models import Cinema

User = get_user_model()


class Movie(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='movies', verbose_name='Кинотеатр')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movies', verbose_name='Владелец')

    title = models.CharField('Название', max_length=120)
    description = models.TextField('Описание', blank=True, null=True)
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)
    release_date = models.DateTimeField()
    trailer = models.FileField('Трейлер', upload_to='files/', null=True, blank=True)
    poster = models.ImageField('Постер', upload_to='images/', null=True, blank=True)
    is_active = models.BooleanField('В прокате', default=True)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title


class ShowTime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='show_time', verbose_name='Фильм')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='show_time', verbose_name='Кинотеатр')

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.start_time} -> {self.end_time}'

    class Meta:
        verbose_name = 'Время показа'
        verbose_name_plural = 'Время показа'
