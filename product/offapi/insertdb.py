"""Clear and fill the database."""

import string
from django.db import transaction, IntegrityError

from product.models import (
    Product,
    Categories,
    NutriscoreGrades,
    Brands,
    CodesProductsOff,
)


def deletedata():
    """Clear datas from Product tables and associates (not Users)."""
    Product.objects.all().delete()
    Categories.objects.all().delete()
    NutriscoreGrades.objects.all().delete()
    Brands.objects.all().delete()
    CodesProductsOff.objects.all().delete()


def insertdb(Api_data):
    """Use Django Orm to fill database."""
    # Fill Nutriscoregrades table
    grades = list(string.ascii_lowercase[0:4])
    i = 1
    for grade in grades:
        NutriscoreGrades.objects.get_or_create(pk=i, nutriscore_grade=grade)
        i += 1

    # Fill Product table and others
    count = 0
    product_count = 0
    for product in Api_data:
        try:
            with transaction.atomic():
                Brands_instance = Brands.objects.get_or_create(
                    brand=product["brands"],
                )
                Categories_instance = Categories.objects.get_or_create(
                    category=product["categories"],
                )
                CodesProductsOff_instance = CodesProductsOff.objects.get_or_create(
                    code=product["code"],
                )
                NutriscoreGrades_instance = NutriscoreGrades.objects.get_or_create(
                    nutriscore_grade=product["nutriscore_grade"],
                )
                Product_instance = Product.objects.get_or_create(
                    product_name_fr=product["product_name_fr"],
                    generic_name_fr=product["generic_name_fr"],
                    fat_100g=product["fat_100g"],
                    saturated_fat_100g=product["saturated-fat_100g"],
                    salt_100g=product["salt_100g"],
                    sugars_100g=product["sugars_100g"],
                    url=product["url"],
                    image_url=product["image_url"],
                    Brands=Brands_instance[0],
                    Categories=Categories_instance[0],
                    CodesProductsOff=CodesProductsOff_instance[0],
                    NutriscoreGrades=NutriscoreGrades_instance[0],
                )
                product_count += 1
        except IntegrityError as exception:
            count += 1
            print("IntegrityError count :", count, exception.args[0])
            pass

