"""Test views for webapp app."""

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

# https://docs.djangoproject.com/fr/3.1/topics/testing/tools/

# https://docs.djangoproject.com/fr/3.1/topics/testing/tools/#django.test.TransactionTestCase

# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from django.test import LiveServerTestCase
# from selenium.webdriver.firefox.webdriver import WebDriver


# class MySeleniumTests(LiveServerTestCase):
#     fixtures = ["user-data.json"]

#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.selenium = WebDriver()
#         cls.selenium.implicitly_wait(10)

#     @classmethod
#     def tearDownClass(cls):
#         cls.selenium.quit()
#         super().tearDownClass()

#     def test_login(self):
#         from selenium.webdriver.support.wait import WebDriverWait

#         timeout = 2
#         self.live_server_url = "https://lepurbeurre.herokuapp.com/"
#         self.selenium.get("%s%s" % (self.live_server_url, "/login/"))
#         username_input = self.selenium.find_element_by_name("username")
#         username_input.send_keys("myuser")
#         password_input = self.selenium.find_element_by_name("password")
#         password_input.send_keys("secret")
#         self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
#         WebDriverWait(self.selenium, timeout).until(
#             lambda driver: driver.find_element_by_tag_name("body")
#         )


# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


# class PythonOrgSearch(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()

#     def test_search_in_python_org(self):
#         driver = self.driver
#         driver.get("http://www.python.org")
#         self.assertIn("Python", driver.title)
#         elem = driver.find_element_by_name("q")
#         elem.send_keys("pycon")
#         elem.send_keys(Keys.RETURN)
#         assert "No results found." not in driver.page_source

#     def tearDown(self):
#         self.driver.close()

from django.test import LiveServerTestCase, Client
from django.contrib.auth import get_user_model
from selenium import webdriver
from django.contrib import auth


class FirefoxFunctionalTestCases(LiveServerTestCase):
    """Functional tests using the Firefox web browser."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()

    # @classmethod
    # def setUpTestData(cls):
    #     """Create test datas."""
    #     # User
    #     name = "user1"
    #     email = "user1@email.com"
    #     psswd = "psswd123"
    #     user = CustomUser.objects.create(
    #         username=name, email=email, password=psswd
    #     )
    #     # Log user
    #     c = Client()
    #     c.login(username=name, password=psswd)
    #     # Query
    #     cls.query = "product_name_fr"
    #     # Product
    #     code = CodesProductsOff.objects.create(code=0)
    #     brand = Brands.objects.create(brand="test_brand")
    #     nutriscore_grade = NutriscoreGrades.objects.create(
    #         nutriscore_grade="c"
    #     )
    #     category = Categories.objects.create(category="test_category")
    #     cls.product = Product.objects.create(
    #         product_name_fr="test_product_name_fr",
    #         generic_name_fr="test_generic_name_fr",
    #         fat_100g=1.1,
    #         saturated_fat_100g=2.2,
    #         salt_100g=3.3,
    #         sugars_100g=4.4,
    #         url="test_url.com2",
    #         image_url="test_url.com2",
    #         CodesProductsOff=code,
    #         Brands=brand,
    #         NutriscoreGrades=nutriscore_grade,
    #         Categories=category,
    #     )
    #     # Favorite for User
    #     favorite = Favorites.objects.create(
    #         Product_id=cls.product.id, CustomUser_id=user.id
    #     )

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="user1", password="mdp123mdp"
        )

    def test_user_can_connect_and_disconnect(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element_by_css_selector("#button-login").click()
        self.driver.find_element_by_css_selector("#id_username").send_keys(
            "user1"
        )
        self.driver.find_element_by_css_selector("#id_password").send_keys(
            "mdp123mdp"
        )
        self.driver.find_element_by_css_selector("#button-submit").click()
        # user = self.driver.user(self.client)
        # self.client.force_login(self.user)
        # self.assertTrue(user.is_authenticated)
        self.driver.find_element_by_css_selector("#button-logout").click()


# class TestWiews(TestCase):
#     """Test views and associated templates."""


#     def test_if_view_delete_return_302(self):
#         """Test delete view.

#         Check if "response.status_code" is "302".
#         """
#     # form method="post" action="{% url 'delete' product_id=product.id %}
#     response = self.client.get(
#         reverse("delete"), self.product.id
#     )
#     self.assertEqual(response.status_code, 302)
#     no templates used (redirect to "myfavorites.html")


# def test_if_view_favorites_return_302(self):
#     """Test favorites view.

#     Check if "response.status_code" is "302".
#     """

#     # form method="post" action="{% url 'favorites' product_id=product.id %}">
#     response = self.client.get(
#         reverse("favorites", {"product_id": self.product.id})
#     )
#     self.assertEqual(response.status_code, 302)
#     # no templates used (redirect to "myfavorites")

