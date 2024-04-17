from django.core.exceptions import ValidationError


def name_starts_with_capital_letter(value):
    if not value[0].isupper():
        raise ValidationError('Name must start with a capital letter!')


def nickname_lt_2_chars(value):
    if len(value) < 2:
        raise ValidationError('Nickname must be at least 2 chars long!')
