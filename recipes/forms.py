from django import forms

# try:
from recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "name",
            "author",
            "description",
            "image",
        ]


# except Exception:
# pass


from recipes.models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["value"]
