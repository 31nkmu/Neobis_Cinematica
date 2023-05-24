# Generated by Django 4.2.1 on 2023-05-24 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cinemas', '0001_initial'),
        ('movies', '0002_movie_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cinema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='cinemas.cinema', verbose_name='Кинотеатр'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
    ]