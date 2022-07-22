from django.forms import ModelForm, DateInput, DateField

from meal_plans.models import MealPlan


class CustomDateInput(DateInput):
    input_type = "date"


class MealPlanForm(ModelForm):
    date = DateField(widget=CustomDateInput)

    class Meta:
        model = MealPlan
        fields = ["name", "recipes", "date"]
