from django.contrib.auth import get_user_model
from django.db import models

from applications.cinemas.models import Cinema
from applications.movies.models import Movie

User = get_user_model()


class Room(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms', verbose_name='Владелец')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='rooms', verbose_name='Кинотеатр')
    movie = models.ManyToManyField(Movie, verbose_name='Фильм')

    number = models.IntegerField('Зал')
    title = models.CharField('Название', max_length=120)
    rows = models.IntegerField('Ряды')
    places = models.IntegerField('Места')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'