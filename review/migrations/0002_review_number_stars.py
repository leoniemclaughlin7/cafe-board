# Generated by Django 3.2.21 on 2023-09-11 20:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='number_stars',
            field=models.PositiveIntegerField(default=5, help_text='Enter a rating from 1 to 5 stars.', validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
