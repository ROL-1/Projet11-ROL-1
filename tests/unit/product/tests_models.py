"""Tests database models for product app."""

from django.test import TestCase

from product.models import (
    CodesProductsOff,
    Brands,
    NutriscoreGrades,
    Categories,
    Product,
)


class ProductModelTest(TestCase):
    """Tests for database models."""

    @classmethod
    def setUpTestData(cls):
        """Create fake datas once for all tests and define 'product'."""
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
            fat_100g="1",
            saturated_fat_100g="2",
            salt_100g="3",
            sugars_100g="4",
            url="url@test.com",
            image_url="urlimage@test.com",
        )
        cls.product = Product.objects.get(id=1)

    def test_product_labels(self):
        """Test labels."""
        fields_list = [
            "CodesProductsOff_id",
            "Brands_id",
            "NutriscoreGrades_id",
            "product_name_fr",
            "generic_name_fr",
            "fat_100g",
            "saturated_fat_100g",
            "salt_100g",
            "sugars_100g",
            "url",
            "image_url",
        ]
        labels_list = [
            "CodesProductsOff",
            "Brands",
            "NutriscoreGrades",
            "product name fr",
            "generic name fr",
            "fat 100g",
            "saturated fat 100g",
            "salt 100g",
            "sugars 100g",
            "url",
            "image url",
        ]
        for field, label in zip(fields_list, labels_list):
            field_label = self.product._meta.get_field(field).verbose_name
            self.assertEquals(field_label, label)

    # max_length #
    def test_product_max_length(self):
        """Test product max length some fields."""
        fields_list = ["product_name_fr", "generic_name_fr"]
        max_lengths_list = [100, 100]
        for field, max_length in zip(fields_list, max_lengths_list):
            field_label = self.product._meta.get_field(field).max_length
            self.assertEquals(field_label, max_length)

    # max_digits #
    def test_product_max_digits(self):
        """Test product max digits for some fields."""
        fields_list = [
            "fat_100g",
            "saturated_fat_100g",
            "salt_100g",
            "sugars_100g",
        ]
        max_digits_list = [5, 5, 5, 5]
        for field, max_digits in zip(fields_list, max_digits_list):
            field_label = self.product._meta.get_field(field).max_digits
            self.assertEquals(field_label, max_digits)

    # decimal_places #
    def test_product_decimal_places(self):
        """Test product decimal places for some fields."""
        fields_list = [
            "fat_100g",
            "saturated_fat_100g",
            "salt_100g",
            "sugars_100g",
        ]
        decimal_places_list = [2, 2, 2, 2]
        for field, decimal_places in zip(fields_list, decimal_places_list):
            field_label = self.product._meta.get_field(field).decimal_places
            self.assertEquals(field_label, decimal_places)

    # __str__ #
    def test_object_name_is_product_name_fr(self):
        """Test product name."""
        expected_object_name = self.product.product_name_fr
        self.assertEquals(expected_object_name, str(self.product))

    def test_object_name_is_category(self):
        """Test category name."""
        categories = Categories.objects.get(id=1)
        expected_object_name = categories.category
        self.assertEquals(expected_object_name, str(categories))


class CodesProductsOffModelTest(TestCase):
    """Test table CodesProductsOFF."""

    def test_code_label(self):
        """Test code label."""
        field_label = CodesProductsOff._meta.get_field("code").verbose_name
        self.assertEquals(field_label, "code")


class BrandsTest(TestCase):
    """Tests table Brands."""

    def test_brand_label(self):
        """Test brand label."""
        field_label = Brands._meta.get_field("brand").verbose_name
        self.assertEquals(field_label, "brand")

    def test_brand_max_length(self):
        """Test brand max length."""
        max_length = Brands._meta.get_field("brand").max_length
        self.assertEquals(max_length, 75)


class NutriscoreGradesTest(TestCase):
    """Tests table NutriscoreGrades."""

    def test_nutriscore_grade_label(self):
        """Test nutriscore_grade label."""
        field_label = NutriscoreGrades._meta.get_field(
            "nutriscore_grade"
        ).verbose_name
        self.assertEquals(field_label, "nutriscore grade")

    def test_nutriscore_grade_max_length(self):
        """Test nutriscore_grade max_length."""
        max_length = NutriscoreGrades._meta.get_field(
            "nutriscore_grade"
        ).max_length
        self.assertEquals(max_length, 1)


class CategoriesTest(TestCase):
    """Tests table Categories."""

    def test_categories_Label(self):
        """Test categories label."""
        fields_list = ["category", "parent_id"]
        labels_list = ["category", "parent"]
        for field, label in zip(fields_list, labels_list):
            field_label = Categories._meta.get_field(field).verbose_name
            self.assertEquals(field_label, label)

    def test_category_max_length(self):
        """Test category max length."""
        max_length = Categories._meta.get_field("category").max_length
        self.assertEquals(max_length, 75)
