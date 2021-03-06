#! /usr/bin/env python3
# coding: utf-8
"""config file for apirequests.py."""

REQUEST_PARAMS = [
    "action=process",
    "tagtype_0=categories",
    "tag_contains_0=contains",
    "json=1",
    "page_size=100",
    "fields=",
]

FIELDS = "generic_name_fr,product_name_fr,sugars_100g,salt_100g,\
saturated-fat_100g,fat_100g,nutriscore_grade,brands,code,categories,url,image_url"

# Add, delete or change categories.
CATEGORIES = ["Pizzas", "Sodas", "Chocolats", "Brioches", "Pains"]

# Minimum number of products by categories.
MIN_PROD = 500
