from django.contrib.auth import get_user_model
from django.db import models

from applications.cinemas.models import Cinema

User = get_user_model()


class Movie(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='movies')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movies')

    title = models.CharField('Название', max_length=120)
    description = models.TextField('Описание', blank=True, null=True)
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    trailer = models.FileField('Трейлер', upload_to='files/', null=True, blank=True)
    poster = models.ImageField('Постер', upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title
