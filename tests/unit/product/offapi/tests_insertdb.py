"""Test insertdb.py from offapi."""
from django.test import TestCase, Client
from django.db import IntegrityError


from product.models import (
    CodesProductsOff,
    Brands,
    NutriscoreGrades,
    Categories,
    Product,
)
from product.offapi.insertdb import deletedata, insertdb
from user.models import CustomUser, Favorites


class TestInsertdb(TestCase):
    """Test views and associated templates."""

    @classmethod
    def setUpTestData(cls):
        """Create test datas."""
        # User
        name = "user1"
        email = "user1@email.com"
        psswd = "psswd123"
        cls.user = CustomUser.objects.create(
            username=name, email=email, password=psswd
        )
        # Product
        code = CodesProductsOff.objects.create(code=0)
        brand = Brands.objects.create(brand="test_brand")
        # create nutriscore grade for substitute (need lower id)
        nutriscore_grade_sub = NutriscoreGrades.objects.create(
            nutriscore_grade="a"
        )
        nutriscore_grade = NutriscoreGrades.objects.create(
            nutriscore_grade="c"
        )
        category = Categories.objects.create(category="test_category")
        cls.product = Product.objects.create(
            product_name_fr="test_product_name_fr",
            generic_name_fr="test_generic_name_fr",
            fat_100g=1.1,
            saturated_fat_100g=2.2,
            salt_100g=3.3,
            sugars_100g=4.4,
            url="test_url.com2",
            image_url="test_url.com2",
            CodesProductsOff=code,
            Brands=brand,
            NutriscoreGrades=nutriscore_grade,
            Categories=category,
        )
        # Create substitute
        code_sub = CodesProductsOff.objects.create(code=1)
        substitute = Product.objects.create(
            product_name_fr="test_product_name_fr2",
            generic_name_fr="test_generic_name_fr2",
            fat_100g=1.1,
            saturated_fat_100g=2.2,
            salt_100g=3.3,
            sugars_100g=4.4,
            url="test_url.com",
            image_url="test_url.com",
            CodesProductsOff=code_sub,
            Brands=brand,
            NutriscoreGrades=nutriscore_grade_sub,
            Categories=category,
        )
        # Favorite for User
        favorite = Favorites.objects.create(
            Product_id=cls.product.id, CustomUser_id=cls.user.id
        )

    def test_deletedata_check_if_table_Product_is_clear(self):
        """Check if datas are deleted in table Product."""
        d = deletedata()
        count = Product.objects.all().count()
        self.assertTrue(count == 0)

    def test_deletedata_check_if_table_Categories_is_clear(self):
        """Check if datas are deleted in table Categories."""
        d = deletedata()
        count = Categories.objects.all().count()
        self.assertTrue(count == 0)

    def test_deletedata_check_if_table_NutriscoreGrades_is_clear(self):
        """Check if datas are deleted in table NutriscoreGrades."""
        d = deletedata()
        count = NutriscoreGrades.objects.all().count()
        self.assertTrue(count == 0)

    def test_deletedata_check_if_table_Brands_is_clear(self):
        """Check if datas are deleted in table Brands."""
        d = deletedata()
        count = Brands.objects.all().count()
        self.assertTrue(count == 0)

    def test_deletedata_check_if_table_CodesProductsOff_is_clear(self):
        """Check if datas are deleted in table CodesProductsOff."""
        d = deletedata()
        count = CodesProductsOff.objects.all().count()
        self.assertTrue(count == 0)

    def test_insertdb(self):
        """Check if data can be loaded from a json, like apirequest.api_get_data give datas."""
        api_results = [
            {
                "categories": "Pizzas",
                "generic_name_fr": "Pizza surgel\u00e9e",
                "code": "3270160717323",
                "product_name_fr": "Les Collections cr\u00e9atives",
                "url": "https://fr.openfoodfacts.org/produit/3270160717323/les-collections-creatives-picard",
                "salt_100g": 1.1,
                "sugars_100g": 2.4,
                "saturated-fat_100g": 3.5,
                "brands": "Picard",
                "nutriscore_grade": "b",
                "fat_100g": 7.2,
                "image_url": "https://static.openfoodfacts.org/images/products/327/016/071/7323/front_fr.27.400.jpg",
            },
            {
                "generic_name_fr": "Pizza",
                "categories": "Pizzas",
                "code": "3242272345053",
                "product_name_fr": "Sodebo Dolce Pizza - 4 Formaggi",
                "url": "https://fr.openfoodfacts.org/produit/3242272345053/sodebo-dolce-pizza-4-formaggi",
                "salt_100g": 1.2,
                "sugars_100g": 2.7,
                "saturated-fat_100g": 4.6,
                "brands": "Sodebo",
                "nutriscore_grade": "c",
                "fat_100g": 7.9,
                "image_url": "https://static.openfoodfacts.org/images/products/324/227/234/5053/front_fr.35.400.jpg",
            },
            {
                "product_name_fr": "Dolce Pizza - Campanella",
                "generic_name_fr": "Pizza p\u00e2te fine garnie de mozzarella, de jambon Speck et de roquette",
                "categories": "Pizzas",
                "code": "3242272345558",
                "url": "https://fr.openfoodfacts.org/produit/3242272345558/dolce-pizza-campanella-sodebo",
                "sugars_100g": 1.8,
                "salt_100g": 1.7,
                "fat_100g": 5.5,
                "nutriscore_grade": "c",
                "image_url": "https://static.openfoodfacts.org/images/products/324/227/234/5558/front_fr.71.400.jpg",
                "brands": "Sodebo,dolce",
                "saturated-fat_100g": 2.9,
            },
            {
                "sugars_100g": 2.6,
                "salt_100g": 0.96,
                "fat_100g": 12.8,
                "nutriscore_grade": "d",
                "image_url": "https://static.openfoodfacts.org/images/products/327/016/083/8110/front_fr.36.400.jpg",
                "saturated-fat_100g": 6.3,
                "brands": "Picard",
                "product_name_fr": "Pizza N\u00b011 - Ch\u00e8vre, miel, noix",
                "generic_name_fr": "Pizza",
                "categories": "Pizzas",
                "code": "3270160838110",
                "url": "https://fr.openfoodfacts.org/produit/3270160838110/pizza-n-11-chevre-miel-noix-picard",
            },
            {
                "product_name_fr": "BUITONI FRAICH'UP pizza surgel\u00e9e 4 Fromages",
                "generic_name_fr": "Pizza surgel\u00e9e",
                "categories": "Pizzas",
                "code": "7613034223852",
                "url": "https://fr.openfoodfacts.org/produit/7613034223852/buitoni-fraich-up-pizza-surgelee-4-fromages",
                "sugars_100g": 2.8,
                "salt_100g": 1.1,
                "fat_100g": 8.6,
                "nutriscore_grade": "c",
                "image_url": "https://static.openfoodfacts.org/images/products/761/303/422/3852/front_fr.48.400.jpg",
                "saturated-fat_100g": 4.4,
                "brands": "Buitoni, Fraich'up",
            },
        ]

        d = deletedata()
        i = insertdb(api_results)
        p = Product.objects.all().count()
        self.assertTrue(p == 5)

