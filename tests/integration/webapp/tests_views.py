"""Tests for views.py from webapp."""

from django.test import TestCase, Client
from django.urls import reverse
from django.template.loader import render_to_string

from product.models import (
    CodesProductsOff,
    Brands,
    NutriscoreGrades,
    Categories,
    Product,
)
from user.models import CustomUser, Favorites


class TestWiews(TestCase):
    """Test views and associated templates."""

    @classmethod
    def setUpTestData(cls):
        """Create test datas."""
        # User
        name = "user1"
        email = "user1@email.com"
        psswd = "psswd123"
        user = CustomUser.objects.create(
            username=name, email=email, password=psswd
        )
        # Query
        cls.query = "product_name_fr"
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
            Product_id=cls.product.id, CustomUser_id=user.id
        )

    def test_if_view_admin_return_302(self):
        """Check if "response.status_code" is "302"."""
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, 302)

    def test_if_view_contact_return_200_and_use_suitables_templates(self):
        """1. Check if "response.status_code" is "200".

        2. Check if suitables templates are used.
        """
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        with self.assertTemplateUsed("webapp/contact.html"):
            render_to_string("webapp/contact.html")
        with self.assertTemplateUsed("webapp/base.html"):
            render_to_string("webapp/contact.html")

    def test_if_view_delete_return_302(self):
        """Check if "response.status_code" is "302"."""
        response = self.client.post(reverse("delete", args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
        # no templates used (redirect to "myfavorites.html")

    def test_if_view_delete_return_200_with_user_logged(self):
        """Check if "response.status_code" is "200" with user logged."""
        self.client.force_login(CustomUser.objects.get_or_create("user1")[0])
        response = self.client.post(reverse("delete", args=[self.product.id]))
        self.assertEqual(response.url, "/webapp/myfavorites/")
        # no templates used (redirect to "myfavorites.html")

    def test_if_view_favorites_return_302(self):
        """Check if "response.status_code" is "302"."""
        response = self.client.post(
            reverse("favorites", args=[self.product.id])
        )
        self.assertEqual(response.status_code, 302)
        # no templates used (redirect to "myfavorites")

    def test_if_view_favorites_return_200_when_user_is_logged(self):
        """Check if "response.status_code" is "200"."""
        self.client.force_login(CustomUser.objects.get_or_create("user1")[0])
        response = self.client.post(
            reverse("favorites", args=[self.product.id])
        )
        self.assertEqual(response.url, "/webapp/myfavorites/")
        # no templates used (redirect to "myfavorites")

    def test_if_view_home_return_200_and_use_suitables_templates(self):
        """1. Check if "response.status_code" is "200".

        2. Check if suitables templates are used.
        """
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        with self.assertTemplateUsed("webapp/home.html"):
            render_to_string("webapp/home.html")
        with self.assertTemplateUsed("webapp/base.html"):
            render_to_string("webapp/home.html")

    def test_if_view_legal_return_200_and_use_suitables_templates(self):
        """1. Check if "response.status_code" is "200".

        2. Check if suitables templates are used.
        """
        response = self.client.get(reverse("legal"))
        self.assertEqual(response.status_code, 200)
        with self.assertTemplateUsed("webapp/legal.html"):
            render_to_string("webapp/legal.html")
        with self.assertTemplateUsed("webapp/base.html"):
            render_to_string("webapp/legal.html")

    def test_if_view_myfavorites_return_302_and_use_suitables_templates(self):
        """1. Check if "response.status_code" is "302".

        2. Check if suitables templates are used.
        """
        response = self.client.get(reverse("myfavorites"))
        self.assertEqual(response.status_code, 302)
        with self.assertTemplateUsed("webapp/myfavorites.html"):
            render_to_string("webapp/myfavorites.html")
        with self.assertTemplateUsed("webapp/base.html"):
            render_to_string("webapp/myfavorites.html")
        with self.assertTemplateUsed("webapp/portfoliobox.html"):
            render_to_string("webapp/myfavorites.html")

    def test_if_view_myfavorites_return_200_with_user_logged(self):
        """Check if myfavorites "response.status_code" is "200" with user logged."""
        self.client.force_login(CustomUser.objects.get_or_create("user1")[0])
        response = self.client.get(reverse("myfavorites"))
        self.assertEqual(response.status_code, 200)

    def test_if_view_product_return_200_and_use_suitables_templates(self):
        """1. Check if "response.status_code" is "200".

        2. Check if suitables templates are used.
        """
        response = self.client.get(reverse("product", args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        with self.assertTemplateUsed("webapp/product.html"):
            render_to_string("webapp/product.html", {"product": self.product,})
        with self.assertTemplateUsed("webapp/base.html"):
            render_to_string("webapp/product.html", {"product": self.product,})

    def test_if_view_results_return_200_and_use_suitables_templates(self):
        """1. Check if "response.status_code" is "200".

        2. Check if suitables templates are used.
        """
        response = self.client.get(
            reverse("results"), {"query": self.product.id}
        )
        self.assertEqual(response.status_code, 200)
        with self.assertTemplateUsed("webapp/results.html"):
            render_to_string("webapp/results.html", {"product": self.product,})
        with self.assertTemplateUsed("webapp/base.html"):
            render_to_string("webapp/results.html", {"product": self.product,})
        with self.assertTemplateUsed("webapp/portfoliobox.html"):
            render_to_string("webapp/results.html", {"product": self.product,})
        self.assertTrue(len(response.context["products"]) == 1)
        self.assertEqual(len(response.context), 3)

    def test_if_view_search_return_200_and_use_suitables_templates(self):
        """1. Check if "response.status_code" is "200".
        
        2. Check if suitables templates are used.
        """
        response = self.client.get(reverse("search"), {"query": self.query})
        self.assertEqual(response.status_code, 200)
        with self.assertTemplateUsed("webapp/search.html"):
            render_to_string("webapp/search.html")
        with self.assertTemplateUsed("webapp/base.html"):
            render_to_string("webapp/search.html")
        with self.assertTemplateUsed("webapp/portfoliobox.html"):
            render_to_string("webapp/search.html")
        self.assertTrue(len(response.context["products"]) > 1)

    def test_myFavorites_page_name_is_not_mesFavoris(self):
        """Check if NoReverseMatch is caused by page named mesFavoris."""
        with self.assertRaises(exceptions.NoReverseMatch):
            self.client.get(reverse("mesFavoris"))

    def test_home_page_name_is_not_index(self):
        """Check if NoReverseMatch is caused by page named index."""
        with self.assertRaises(exceptions.NoReverseMatch):
            self.client.get(reverse("index"))
