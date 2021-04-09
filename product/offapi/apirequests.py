#! /usr/bin/env python3
# coding: utf-8
"""class to get informations from API."""

import json
import re
import requests

from product.offapi.apiconfig import (
    CATEGORIES,
    FIELDS,
    MIN_PROD,
    REQUEST_PARAMS,
)


class ApiRequests:
    """Create requests for api."""

    def __init__(self, Fields_charmax=None):
        # TC def __init__(self):
        """Get datas from API by looping on each category until it's filled."""
        self.scraped = []
        self.cleaned_scraped = []
        self.endpoint = "https://fr.openfoodfacts.org/cgi/search.pl?"
        self.page_nb = 1

    def api_request(self, category):
        """Get datas from api by creating endpoint with parameters."""
        params = (
            "&".join(REQUEST_PARAMS)
            + FIELDS
            + "&page="
            + str(self.page_nb)
            + "&tag_0="
        )
        request = requests.get(self.endpoint + params + category)
        return request

    def add_scraped(self, request):
        """Add products in list scraped."""
        if request.status_code == 500:
            print("Error 500 !")
        else:
            load = json.loads(request.text)
            for product in load["products"]:
                self.scraped.append(product)

    def define_category(self, product):
        """Check 1 : Change 'categories' to class the product in database."""
        search_category = True
        i = 0
        while search_category and i < len(CATEGORIES):
            for category in CATEGORIES:
                if category in product["categories"].split(", "):
                    product["categories"] = category
                    search_category = False
                i += 1
        if search_category:
            product["categories"] = ""

    def wrong_caracters(self, product):
        """Check 2 : Empty string if there is a forbiden caracter."""
        for field, string in product.items():
            if isinstance(string, str):
                match = bool(
                    re.search(r"\t", string)
                    or re.search(r"\n", string)
                    or re.search(r"\r", string)
                )
                if match:
                    product[field] = ""

    def data_missing(self, product):
        """Check 3 : if field or data is missing."""
        # Field missing
        for field in FIELDS.split(","):
            if field not in product.keys():
                return "False"
        # String missing
        for string in product.values():
            if string == "":
                return "False"

    def string_length(self, Fields_charmax, product):
        """Check 4 : if string is too long for database field."""
        for field, string in product.items():
            # Check for fields with characters_max().
            if field in Fields_charmax.keys():
                # Check for element with max length for 'stores'.
                # if field == "stores":
                #     if (
                #         len(max(string.split(","), key=len))
                #         > Fields_charmax[field]
                #     ):
                #         return "False"
                # else:
                if len(string) > Fields_charmax[field]:
                    return "False"

    def products_nb(self, cleaned_scraped, category):
        """Check how many products by categories are suitables."""
        products_nb = 0
        for product in cleaned_scraped:
            if category == product["categories"]:
                products_nb += 1
        if products_nb < MIN_PROD:
            cat_filled = False
        else:
            print(category, "filled")
            cat_filled = True
        return cat_filled

    def api_get_data(self, Fields_charmax):
        # TC def api_get_data(self):
        """Review categories until there is 'MIN_PROD' products for each."""
        print("Loading datas from api.")
        for category in CATEGORIES:
            cat_filled = False
            # Loop while there is not enough products for the category.
            while cat_filled is False:
                # Create request.
                request = self.api_request(category)
                # Add products from the request to 'scraped' list.
                self.add_scraped(request)
                # Review products.
                for product in self.scraped:
                    # Change "categories" product field for only one category.
                    self.define_category(product)
                    # Erease string if there is a forbidden character.
                    self.wrong_caracters(product)
                    # Check datas.
                    Data = self.data_missing(product)
                    Strings = self.string_length(Fields_charmax, product)
                    # Fill 'cleaned_scraped' list, if all checks are trues.
                    if (
                        ("categories" in product)
                        and (category in product["categories"])
                        and (Data != "False")
                        and (Strings != "False")
                    ):
                        self.cleaned_scraped.append(product)
                # Check how many products by categories are suitables.
                cat_filled = self.products_nb(self.cleaned_scraped, category)
                if cat_filled is False:
                    self.page_nb += 1
                else:
                    self.page_nb = 1

        # # Write JSON of datas (for debug)
        # with open("cleaned_scraped.json", "w") as write_file:
        #     json.dump(self.cleaned_scraped, write_file, indent=4)

        return self.cleaned_scraped
