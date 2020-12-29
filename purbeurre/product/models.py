from django.db import models

class Product(models.Model):
    product_name_fr = models.CharField(max_length=100)
    generic_name_fr = models.CharField(max_length=100)
    description = models.TextField()
    fat_100g = models.DecimalField(max_digits=5, decimal_places=2)
    satured-fat_100g = models.DecimalField(max_digits=5, decimal_places=2)
    salt_100g = models.DecimalField(max_digits=5, decimal_places=2)
    sugars_100g = models.DecimalField(max_digits=5, decimal_places=2)
    url = models.URLField()
    image_url = models.URLField()
    CodesProductsOff = models.ForeignKey(CodesProductsOff, on_delete=models.CASCADE)
    Brands = models.ForeignKey(Brands, on_delete=models.DO_NOTHING)
    NutriscroreGrades = models.ForeignKey(NutriscroreGrades, on_delete=models.DO_NOTHING)
    Categories = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)

    def __str__(self):
       return self.product_name_fr

class CodesProductsOff(models.Model):
    code = PositiveBigIntegerField()

class Brands(models.Model):
    brands = models.CharField(max_length=75)

class NutriscroreGrades(models.Model):
    nutriscore_grade = models.CharField(max_length=1)

class Categories(models.Model):
    category = models.CharField(max_length=75)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
       return self.category