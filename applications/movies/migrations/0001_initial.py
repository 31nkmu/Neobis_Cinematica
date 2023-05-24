# Generated by Django 4.2.1 on 2023-05-22 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cinemas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('release_date', models.DateTimeField()),
                ('trailer', models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Трейлер')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Постер')),
                ('is_active', models.BooleanField(default=True, verbose_name='В прокате')),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='cinemas.cinema')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='ShowTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='show_time', to='cinemas.cinema', verbose_name='Кинотеатр')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='show_time', to='movies.movie', verbose_name='Фильм')),
            ],
            options={
                'verbose_name': 'Время показа',
                'verbose_name_plural': 'Время показа',
            },
        ),
    ]