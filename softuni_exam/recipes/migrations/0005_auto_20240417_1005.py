# Generated by Django 3.2.25 on 2024-04-17 07:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20240417_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveIntegerField(help_text='Provide the cooking time in minutes.', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Cooking Time'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cuisine_type',
            field=models.CharField(choices=[('French', 'French'), ('Chinese', 'Chinese'), ('Italian', 'Italian'), ('Balkan', 'Balkan'), ('Other', 'Other')], max_length=7, verbose_name='Cuisine Type'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image_url',
            field=models.URLField(blank=True, null=True, verbose_name='Image URL'),
        ),
    ]
