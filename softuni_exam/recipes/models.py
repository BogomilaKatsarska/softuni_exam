from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from softuni_exam.recipes.validators import nickname_lt_2_chars, name_starts_with_capital_letter


class Profile(models.Model):
    LAST_NAME_MAX_LEN = 30
    FIRST_NAME_MAX_LEN = 30
    NICKNAME_MAX_LEN = 20
    nickname = models.CharField(
        max_length=20,
        validators=(
            nickname_lt_2_chars,
        ),
        unique=True,
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            name_starts_with_capital_letter,
        ),
        verbose_name='First Name',
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            name_starts_with_capital_letter,
        ),
        verbose_name='Last Name',
        null=False,
        blank=False,
    )
    chef = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
    Bio = models.TextField(
        null=True,
        blank=True,
    )


class Recipe(models.Model):
    FRENCH = 'French'
    CHINESE = 'Chinese'
    ITALIAN = 'Italian'
    BALKAN = 'Balkan'
    OTHER = 'Other'

    CUISINES = (
        (FRENCH, FRENCH),
        (CHINESE, CHINESE),
        (ITALIAN, ITALIAN),
        (BALKAN, BALKAN),
        (OTHER, OTHER),
    )

    CUISINE_TYPE_MAX_LEN = 7
    TITLE_MAX_LEN = 100
    TITLE_MIN_LEN = 10
    COOKING_TIME_MIN_VALUE = 1
    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        validators=(
            MinLengthValidator(TITLE_MIN_LEN),
        ),
        unique=True,
        null=False,
        blank=False,
    )
    cuisine_type = models.CharField(
        max_length=CUISINE_TYPE_MAX_LEN,
        choices=CUISINES,
        verbose_name='Cuisine Type',
        null=False,
        blank=False,
    )
    ingredients = models.TextField(
        help_text="Ingredients must be separated by a comma and space.",
        null=False,
        blank=False,
    )
    instructions = models.TextField(
        null=False,
        blank=False,
    )
    cooking_time = models.PositiveIntegerField(
        help_text="Provide the cooking time in minutes.",
        validators=(
            MinValueValidator(COOKING_TIME_MIN_VALUE),
        ),
        verbose_name='Cooking Time',
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        verbose_name='Image URL',
        null=True,
        blank=True,
    )