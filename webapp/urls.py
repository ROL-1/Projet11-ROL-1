from django.urls import path

from . import views


# app_name = "webapp"  # alias webapp :

# Autocomplete
from dal import autocomplete

from django.conf.urls import url

from .views import ProductAutocomplete


urlpatterns = [
    path("contact/", views.contact, name="contact"),
    path("delete/<int:product_id>/", views.delete, name="delete"),
    path("favorites/<int:product_id>/", views.favorites, name="favorites"),
    path("legal/", views.legal, name="legal"),
    path("myfavorites/", views.myfavorites, name="myfavorites"),
    path("product/", views.product, name="product"),
    path("results/", views.results, name="results"),
    path("search/", views.search, name="search"),
    url(
        r"^product-autocomplete/$",
        ProductAutocomplete.as_view(),
        name="product-autocomplete",
    ),
]
