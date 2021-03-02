"""models for user app."""

from django.db import models
from django.contrib.auth.models import AbstractUser
from product.models import Product


class CustomUser(AbstractUser):
    """Custom user model from django."""

    pass


class Favorites(models.Model):
    """Favorites model from django."""

    Product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    CustomUser = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
