# Generated by Django 4.2.1 on 2023-05-24 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_remove_ticket_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket_type',
            field=models.CharField(choices=[('children', 'children'), ('student', 'student'), ('adult', 'adult')], default=12312412431),
            preserve_default=False,
        ),
    ]
