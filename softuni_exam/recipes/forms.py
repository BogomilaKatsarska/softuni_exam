from django import forms
from softuni_exam.recipes.models import Profile, Recipe


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('nickname', 'first_name', 'last_name', 'chef')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Recipe.objects.all().delete()
        else:
            return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

        widgets = {
            'ingredients': forms.Textarea(
                attrs={
                    'placeholder': 'ingredient1, ingredient2, ...',
                }
            ),
            'instructions': forms.Textarea(
                attrs={
                    'placeholder': 'Enter detailed instructions here...',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Optional image URL here...',
                }
            ),
        }


class RecipeEditForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

        widgets = {
            'ingredients': forms.Textarea(
                attrs={
                    'placeholder': 'ingredient1, ingredient2, ...',
                }
            ),
            'instructions': forms.Textarea(
                attrs={
                    'placeholder': 'Enter detailed instructions here...',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Optional image URL here...',
                }
            ),
        }


class RecipeDeleteForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'ingredients': forms.Textarea(
                attrs={
                    'placeholder': 'ingredient1, ingredient2, ...',
                }
            ),
            'instructions': forms.Textarea(
                attrs={
                    'placeholder': 'Enter detailed instructions here...',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Optional image URL here...',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for _,field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
