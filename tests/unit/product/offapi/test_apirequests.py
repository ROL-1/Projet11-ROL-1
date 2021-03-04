"""Tests file for api_requests.py. With Pytest."""

from product.offapi.api_requests import ApiRequests


class TestApiRequests:
    """Test for class : Command."""

    # @classmethod
    # def setUpTestData(cls):
    #     """Create test datas."""

    def test_api_get_data(self, monkeypatch):
        # Fake datas
        charmax_res = {
            "generic_name_fr": 100,
            "product_name_fr": 100,
            "url": 200,
            "image_url": 200,
            "categories": 75,
            "brands": 75,
        }

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

        def mock_api_get_data(self):
            """Mock function for ApiRequests."""
            return api_results

        monkeypatch.setattr(ApiRequests, "api_get_data", mock_api_get_data)

        Api_data = ApiRequests().api_get_data()

        assert Api_data == api_results
