# Generated by Django 4.2.1 on 2023-05-24 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='card_balance',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='card_number',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
    ]
