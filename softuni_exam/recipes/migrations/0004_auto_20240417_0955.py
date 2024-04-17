# Generated by Django 3.2.25 on 2024-04-17 06:55

from django.db import migrations, models
import softuni_exam.recipes.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=30, validators=[softuni_exam.recipes.validators.name_starts_with_capital_letter], verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=30, validators=[softuni_exam.recipes.validators.name_starts_with_capital_letter], verbose_name='Last Name'),
        ),
    ]
