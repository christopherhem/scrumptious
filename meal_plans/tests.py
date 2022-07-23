from django.test import TestCase
from meal_plans.models import MealPlan
from django.utils import timezone
from django.db.utils import IntegrityError
from django.contrib.auth.models import User


class MealPlanTestCase(TestCase):
    def test_meal_plans_must_have_a_user(self):
        # Arrange
        with self.assertRaises(IntegrityError):
            MealPlan.objects.create(
                name="This weeks", date=timezone.now(), owner=None
            )

    def test_meal_plans_need_to_set_name_properly(self):
        # Arrange
        name = "My Meal Plan"
        owner = User.objects.create(username="test_user")
        print(name)

        # Act
        meal_plan = MealPlan.objects.create(
            name=name, date=timezone.now(), owner=owner
        )
        # Assert
        self.assertEqual(meal_plan.name, name)
