from django.contrib.auth import get_user_model
from django.db import models

from applications.cinemas.models import Cinema
from applications.movies.models import Movie

User = get_user_model()


class Room(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='rooms', verbose_name='Кинотеатр')

    number = models.IntegerField('Зал')
    title = models.CharField('Название', max_length=120)
    rows = models.IntegerField('Ряды')
    places = models.IntegerField('Места')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'


class Seat(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seats', verbose_name='Владелец')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='seats', verbose_name='Зал')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='seats', verbose_name='Кинотеатр')

    place = models.IntegerField('Ряд')
    row = models.IntegerField('Место')

    def __str__(self):
        return f'ряд {self.place} место {self.row}'

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
