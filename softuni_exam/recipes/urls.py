from django.urls import path

from softuni_exam.recipes.views import index, catalogue, recipe_create, recipe_details, recipe_edit, recipe_delete, \
    profile_create, profile_details, profile_edit, profile_delete

urlpatterns = (
    path('', index, name='index'),
    path('recipe/catalogue/', catalogue, name='catalogue'),
    path('recipe/create/', recipe_create, name='recipe create'),
    path('recipe/<int:pk>/details/', recipe_details, name='recipe details'),
    path('recipe/<int:pk>/edit/', recipe_edit, name='recipe edit'),
    path('recipe/<int:pk>/delete/', recipe_delete, name='recipe delete'),
    path('profile/create/', profile_create, name='profile create'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/edit/', profile_edit, name='profile edit'),
    path('profile/delete/', profile_delete, name='profile delete'),
)