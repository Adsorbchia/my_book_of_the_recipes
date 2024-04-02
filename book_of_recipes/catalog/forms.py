from django import forms
from catalog.models import Recipe


class UserRecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = [
            'name_recipe',
            'slug',
            'description',
            'ingredients',
            'cooking_steps',
            'cooking_time',
            'image', 
            'category','author' ]
    image = forms.ImageField(required=False)
