#! /usr/bin/env python3
# coding: utf-8
"""Class to retrives informations from database."""

# from .api_config import FIELDS

from product.models import (
    Product,
    Categories,
    Brands,
)


class Charmax:
    """Requests for questioning database."""

    def characters_max():
        """Retrieve the maximum number of characters for the fields."""
        PRODUCT_FIELDS = "generic_name_fr,product_name_fr,url,image_url"

        char_max = {}
        for field in PRODUCT_FIELDS.split(","):
            data = Product._meta.get_field(field).max_length
            dict_data = {field: data}
            if data != None:
                char_max.update(dict_data)
        data_cat = Categories._meta.get_field("category").max_length
        if data_cat != None:
            char_max.update({"categories": data_cat})
        data_brand = Brands._meta.get_field("brand").max_length
        if data_brand != None:
            char_max.update({"brands": data_brand})
        return char_max
