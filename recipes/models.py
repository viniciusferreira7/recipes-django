from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=65)


class PreparationTimeUnit(models.TextChoices):
    MINUTE = "MIN", "Minute"
    HOUR = "H", "Hour"
    DAY = "D", "Day"


class ServingUnit(models.TextChoices):
    GRAM = "G", "Gram"
    MILLILITER = "ML", "Milliliter"
    UNIT = "UN", "Unit"
    SLICE = "SL", "Slice"


class Recipe(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField(unique=True)
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(
        max_length=30,
        choices=PreparationTimeUnit.choices,
        default=PreparationTimeUnit.MINUTE
    )
    servings = models.IntegerField()
    servings_unit = models.CharField(
        max_length=30,
        choices=ServingUnit.choices,
        default=ServingUnit.UNIT
    )
    preparation_steps = models.TextField()
    is_preparation_steps_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to="recipes/covers/%Y/%m/%d/")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
    ),
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
