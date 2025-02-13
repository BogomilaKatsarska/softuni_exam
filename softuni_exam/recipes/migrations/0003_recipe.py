# Generated by Django 3.2.25 on 2024-04-17 06:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20240417_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('cuisine_type', models.CharField(choices=[('French', 'French'), ('Chinese', 'Chinese'), ('Italian', 'Italian'), ('Balkan', 'Balkan'), ('Other', 'Other')], max_length=7)),
                ('ingredients', models.TextField(help_text='Ingredients must be separated by a comma and space.')),
                ('instructions', models.TextField()),
                ('cooking_time', models.PositiveIntegerField(help_text='Provide the cooking time in minutes.', validators=[django.core.validators.MinValueValidator(1)])),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
