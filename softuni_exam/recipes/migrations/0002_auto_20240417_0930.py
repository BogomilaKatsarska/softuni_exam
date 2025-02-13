# Generated by Django 3.2.25 on 2024-04-17 06:30

from django.db import migrations, models
import softuni_exam.recipes.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=30, validators=[softuni_exam.recipes.validators.name_starts_with_capital_letter]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=30, validators=[softuni_exam.recipes.validators.name_starts_with_capital_letter]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(max_length=20, unique=True, validators=[softuni_exam.recipes.validators.nickname_lt_2_chars]),
        ),
    ]
