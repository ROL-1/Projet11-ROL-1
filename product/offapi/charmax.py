#! /usr/bin/env python3
# coding: utf-8
"""Class to retrives informations from database."""

# from .api_config import FIELDS

from product.models import (
    Product,
    Categories,
    NutriscoreGrades,
    Brands,
    CodesProductsOff,
)


class Charmax:
    """Requests for questioning database."""

    def characters_max():
        """Retrieve the maximum number of characters for the fields."""
        FIELDS = "generic_name_fr,product_name_fr,sugars_100g,salt_100g,\
saturated_fat_100g,fat_100g,url,image_url"

        char_max = {}
        for field in FIELDS.split(","):
            print(field)
            # data = self.Log.request(
            #     """SELECT column_name, character_maximum_length
            #     FROM information_schema.columns WHERE column_name = '%s'
            #     AND (DATA_TYPE = 'char' OR DATA_TYPE = 'varchar')"""
            #     % (field)
            # )
            data = Product._meta.get_field(field).max_length
            dict_data = {field: data}
            if data != None:
                char_max.update(dict_data)
            print(char_max)
        return char_max
