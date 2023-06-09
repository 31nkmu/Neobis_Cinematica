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
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Зал')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('rows', models.IntegerField(verbose_name='Ряды')),
                ('places', models.IntegerField(verbose_name='Места')),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='cinemas.cinema', verbose_name='Кинотеатр')),
            ],
            options={
                'verbose_name': 'Зал',
                'verbose_name_plural': 'Залы',
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.IntegerField(verbose_name='Ряд')),
                ('row', models.IntegerField(verbose_name='Место')),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='cinemas.cinema', verbose_name='Кинотеатр')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='rooms.room', verbose_name='Зал')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
            },
        ),
    ]
