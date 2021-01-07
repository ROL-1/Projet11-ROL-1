from django.test import TestCase

from product.models import (
    CodesProductsOff,
    Brands,
    NutriscoreGrades,
    Categories,
    Product,
)


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CodesProductsOff.objects.create(code="8000070200289"),
        Brands.objects.create(brand="brandtest"),
        NutriscoreGrades.objects.create(nutriscore_grade="a"),
        Categories.objects.create(category="categorytest"),
        Product.objects.create(
            CodesProductsOff_id="1",
            Brands_id="1",
            NutriscoreGrades_id="1",
            Categories_id="1",
            product_name_fr="product name test",
            generic_name_fr="generic name test",
            description="descriptiontest",
            fat_100g="1",
            satured_fat_100g="2",
            salt_100g="3",
            sugars_100g="4",
            url="url@test.com",
            image_url="urlimage@test.com",
        )

    def setUp(self):
        print(
            " setUp: Run once for every test method to setup clean data. Utilisé ici non pour clean, mais pour éviter répétition : ok ?"
        )
        self.product = Product.objects.get(id=1)
        pass

    # Label #
    def test_product_name_fr_label(self):
        field_label = self.product._meta.get_field(
            "product_name_fr"
        ).verbose_name
        self.assertEquals(field_label, "product name fr")

    def test_generic_name_fr_label(self):
        field_label = self.product._meta.get_field(
            "generic_name_fr"
        ).verbose_name
        self.assertEquals(field_label, "generic name fr")

    def test_description_label(self):
        field_label = self.product._meta.get_field("description").verbose_name
        self.assertEquals(field_label, "description")

    def test_fat_100g_label(self):
        field_label = self.product._meta.get_field("fat_100g").verbose_name
        self.assertEquals(field_label, "fat 100g")

    def test_satured_fat_100g_label(self):
        field_label = self.product._meta.get_field(
            "satured_fat_100g"
        ).verbose_name
        self.assertEquals(field_label, "satured fat 100g")

    def test_salt_100g_label(self):
        field_label = self.product._meta.get_field("salt_100g").verbose_name
        self.assertEquals(field_label, "salt 100g")

    def test_sugars_100g_label(self):
        field_label = self.product._meta.get_field("sugars_100g").verbose_name
        self.assertEquals(field_label, "sugars 100g")

    def test_url_label(self):
        field_label = self.product._meta.get_field("url").verbose_name
        self.assertEquals(field_label, "url")

    def test_image_url_label(self):
        field_label = self.product._meta.get_field("image_url").verbose_name
        self.assertEquals(field_label, "image url")

    def test_CodesProductsOff_label(self):
        field_label = self.product._meta.get_field(
            "CodesProductsOff"
        ).verbose_name
        self.assertEquals(field_label, "CodesProductsOff")

    def test_Brands_label(self):
        field_label = self.product._meta.get_field("Brands").verbose_name
        self.assertEquals(field_label, "Brands")

    def test_NutriscoreGrades_label(self):
        field_label = self.product._meta.get_field(
            "NutriscoreGrades"
        ).verbose_name
        self.assertEquals(field_label, "NutriscoreGrades")

    def test_Categories_label(self):
        field_label = self.product._meta.get_field("Categories").verbose_name
        self.assertEquals(field_label, "Categories")

    # max_length #
    def test_product_name_fr_max_length(self):
        max_length = self.product._meta.get_field("product_name_fr").max_length
        self.assertEquals(max_length, 100)

    def test_generic_name_fr_max_length(self):
        max_length = self.product._meta.get_field("generic_name_fr").max_length
        self.assertEquals(max_length, 100)

    # max_digits #
    def test_fat_100g_max_digits(self):
        max_digits = self.product._meta.get_field("fat_100g").max_digits
        self.assertEquals(max_digits, 5)

    def test_satured_fat_100g_max_digits(self):
        max_digits = self.product._meta.get_field(
            "satured_fat_100g"
        ).max_digits
        self.assertEquals(max_digits, 5)

    def test_salt_100g_max_digits(self):
        max_digits = self.product._meta.get_field("salt_100g").max_digits
        self.assertEquals(max_digits, 5)

    def test_sugars_100g_max_digits(self):
        max_digits = self.product._meta.get_field("sugars_100g").max_digits
        self.assertEquals(max_digits, 5)

    # decimal_places #
    def test_fat_100g_decimal_places(self):
        decimal_places = self.product._meta.get_field(
            "fat_100g"
        ).decimal_places
        self.assertEquals(decimal_places, 2)

    def test_satured_fat_100g_decimal_places(self):
        decimal_places = self.product._meta.get_field(
            "satured_fat_100g"
        ).decimal_places
        self.assertEquals(decimal_places, 2)

    def test_salt_100g_decimal_places(self):
        decimal_places = self.product._meta.get_field(
            "salt_100g"
        ).decimal_places
        self.assertEquals(decimal_places, 2)

    def test_sugars_100g_decimal_places(self):
        decimal_places = self.product._meta.get_field(
            "sugars_100g"
        ).decimal_places
        self.assertEquals(decimal_places, 2)

    # __str__ #
    def test_object_name_is_product_name_fr(self):
        expected_object_name = self.product.product_name_fr
        self.assertEquals(expected_object_name, str(self.product))


class CodesProductsOffModelTest(TestCase):
    # Label #
    def test_code_label(self):
        field_label = CodesProductsOff._meta.get_field("code").verbose_name
        self.assertEquals(field_label, "code")


class BrandsTest(TestCase):
    # Label #
    def test_brand_label(self):
        field_label = Brands._meta.get_field("brand").verbose_name
        self.assertEquals(field_label, "brand")

    # max_length #
    def test_brand_max_length(self):
        max_length = Brands._meta.get_field("brand").max_length
        self.assertEquals(max_length, 75)


class NutriscoreGradesTest(TestCase):
    # Label #
    def test_nutriscore_grade_label(self):
        field_label = NutriscoreGrades._meta.get_field(
            "nutriscore_grade"
        ).verbose_name
        self.assertEquals(field_label, "nutriscore grade")

    # max_length #
    def test_nutriscore_grade_max_length(self):
        max_length = NutriscoreGrades._meta.get_field(
            "nutriscore_grade"
        ).max_length
        self.assertEquals(max_length, 1)


class CategoriesTest(TestCase):
    # Label #
    def test_category_label(self):
        field_label = Categories._meta.get_field("category").verbose_name
        self.assertEquals(field_label, "category")

    def test_parent_label(self):
        field_label = Categories._meta.get_field("parent_id").verbose_name
        self.assertEquals(field_label, "parent")

    # max_length #
    def test_category_max_length(self):
        max_length = Categories._meta.get_field("category").max_length
        self.assertEquals(max_length, 75)

    # # __str__ # ????????
    # def test_object_name_is_category(self):
    #     categories = Categories.objects.get(id=1)
    #     expected_object_name = categories.category
    #     self.assertEquals(expected_object_name, str(categories))


# Les classes de test ont aussi une méthode tearDown():
#  que nous n'avons pas utilisée. Cette méthode n'est pas particulièrement utile pour les tests
#  avec bases de données, dans la mesure où la classe de base TestCase prend soin pour vous de
#  supprimer la base de données utilisées pour les tests.

