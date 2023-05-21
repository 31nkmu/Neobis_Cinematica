from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Cinema(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cinemas', verbose_name='Владелец')

    title = models.CharField('название', max_length=120)
    address = models.CharField('адрес', max_length=120)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'кинотеатр'
        verbose_name_plural = 'кинотеатры'
