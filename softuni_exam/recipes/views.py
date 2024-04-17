from django.shortcuts import render, redirect
from softuni_exam.recipes.forms import ProfileCreateForm, RecipeCreateForm, RecipeEditForm, RecipeDeleteForm, \
    ProfileDeleteForm, ProfileEditForm
from softuni_exam.recipes.models import Profile, Recipe


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        has_profile = False
    else:
        has_profile = True
    context = {
        'has_profile': has_profile,
    }
    return render(request, 'home-page.html', context)


def catalogue(request):
    profile = get_profile()
    if profile is None:
        has_profile = False
    else:
        has_profile = True
    if profile is None:
        return profile_create(request)

    context = {
        'recipes': Recipe.objects.all(),
        'has_profile': has_profile,
    }
    return render(request, 'catalogue.html', context)


def recipe_create(request):
    profile = get_profile()
    if profile is None:
        has_profile = False
    else:
        has_profile = True
    if request.method == 'POST':
        form = RecipeCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = RecipeCreateForm()

    context = {
        'form': form,
        'has_profile': has_profile,
    }
    return render(request, 'create-recipe.html', context)


def recipe_details(request, pk):
    profile = get_profile()
    if profile is None:
        has_profile = False
    else:
        has_profile = True
    recipe = Recipe.objects.filter(pk=pk).get()
    all_ingredients = recipe.ingredients.split(', ')

    context = {
        'recipe': recipe,
        'has_profile': has_profile,
        'all_ingredients': all_ingredients,
    }
    return render(request, 'details-recipe.html', context)


def recipe_edit(request, pk):
    profile = get_profile()
    if profile is None:
        has_profile = False
    else:
        has_profile = True
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecipeEditForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = RecipeEditForm(instance=recipe)

    context = {
        'form': form,
        'recipe': recipe,
        'has_profile': has_profile,
    }
    return render(request, 'edit-recipe.html', context)


def recipe_delete(request, pk):
    profile = get_profile()
    if profile is None:
        has_profile = False
    else:
        has_profile = True
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecipeDeleteForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = RecipeDeleteForm(instance=recipe)

    context = {
        'form': form,
        'recipe': recipe,
        'has_profile': has_profile,
    }
    return render(request, 'delete-recipe.html', context)


def profile_create(request):
    profile = get_profile()
    if profile is None:
        has_profile = False
    else:
        has_profile = True

    if get_profile() is not None:
        return redirect('index')
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'has_profile': has_profile,
    }
    return render(request, 'create-profile.html', context)


def profile_details(request):
    profile = get_profile()
    if profile is None:
        has_profile = False
    else:
        has_profile = True
    recipes_count = Recipe.objects.count()
    context = {
        'profile': profile,
        'recipes_count': recipes_count,
        'has_profile': has_profile,
    }
    return render(request, 'details-profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if profile is None:
        has_profile = False
    else:
        has_profile = True

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form,
        'has_profile': has_profile,
    }
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }

    return render(request, 'delete-profile.html', context)
