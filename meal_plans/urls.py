from django.urls import path

from meal_plans.views import (
    MealPlanView,
    MealPlanDetailView,
    MealPlanCreateView,
    MealPlanDeleteView,
    MealPlanUpdateView,
)

urlpatterns = [
    path("", MealPlanView.as_view(), name="meal_plan_list"),
    path("<int:pk>/", MealPlanDetailView.as_view(), name="meal_plan_detail"),
    path(
        "<int:pk>/delete/",
        MealPlanDeleteView.as_view(),
        name="meal_plan_delete",
    ),
    path("new/", MealPlanCreateView.as_view(), name="meal_plan_new"),
    path("<int:pk>/edit/", MealPlanUpdateView.as_view(), name="meal_plan_edit"),
]
