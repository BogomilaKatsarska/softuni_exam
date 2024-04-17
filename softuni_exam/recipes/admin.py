from django.contrib import admin
from softuni_exam.recipes.models import Profile, Recipe


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass
