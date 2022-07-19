from django.db import models
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20)
    author = models.ForeignKey(
        USER_MODEL, related_name="tags", on_delete=models.CASCADE, null=True
    )
    recipes = models.ManyToManyField("recipes.Recipe", related_name="tags")
