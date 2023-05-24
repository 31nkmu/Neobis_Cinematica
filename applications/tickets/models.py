from django.contrib.auth import get_user_model
from django.db import models

from applications.cinemas.models import Cinema
from applications.movies.models import Movie
from applications.rooms.models import Room, Seat

User = get_user_model()


class Ticket(models.Model):
    movie = models.ForeignKey(Movie, related_name='tickets', on_delete=models.CASCADE, verbose_name='Фильм')
    cinema = models.ForeignKey(Cinema, related_name='tickets', on_delete=models.CASCADE, verbose_name='Кинотеатр')
    room = models.ForeignKey(Room, related_name='tickets', on_delete=models.CASCADE, verbose_name='Зал')
    seat = models.ForeignKey(Seat, related_name='tickets', on_delete=models.CASCADE, verbose_name='Место')
    owner = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE, verbose_name='Покупатель')

    purchase_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cinema} -> {self.movie}'

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
