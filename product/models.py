"""Models for the database. Create tables and fields."""

from django.db import models


class CodesProductsOff(models.Model):
    """Table for codes from OpenFoodFact (could be change to use an other api)."""

    code = models.PositiveBigIntegerField(unique=True)


class Brands(models.Model):
    """Table for brands."""

    brand = models.CharField(max_length=75, unique=True)


class NutriscoreGrades(models.Model):
    """Table for nutriscoregrades.

    Will be filled first when 'databse' command is called.
    Letters must be filled in order for the algorithm to work.
    """

    nutriscore_grade = models.CharField(max_length=1, unique=True)


class Categories(models.Model):
    """Table for categories.
    
    Parents categories could be add.
    """

    category = models.CharField(max_length=75, unique=True)
    parent = models.ForeignKey(
        "self", on_delete=models.DO_NOTHING, null=True, blank=True
    )

    def __str__(self):
        """Define name display."""
        return self.category


class Product(models.Model):
    """Table for products."""

    product_name_fr = models.CharField(max_length=100, unique=True)
    generic_name_fr = models.CharField(max_length=100)
    fat_100g = models.DecimalField(max_digits=5, decimal_places=2)
    saturated_fat_100g = models.DecimalField(max_digits=5, decimal_places=2)
    salt_100g = models.DecimalField(max_digits=5, decimal_places=2)
    sugars_100g = models.DecimalField(max_digits=5, decimal_places=2)
    url = models.URLField(unique=True)
    image_url = models.URLField()
    CodesProductsOff = models.ForeignKey(
        CodesProductsOff, on_delete=models.CASCADE
    )
    Brands = models.ForeignKey(Brands, on_delete=models.DO_NOTHING)
    NutriscoreGrades = models.ForeignKey(
        NutriscoreGrades, on_delete=models.DO_NOTHING
    )
    Categories = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)

    def __str__(self):
        """Define name display."""
        return self.product_name_fr

