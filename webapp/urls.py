"""urls for webapp app."""

from django.urls import path
from django.conf.urls import url
from . import views
from .views import ProductAutocomplete

urlpatterns = [
    path("contact/", views.contact, name="contact"),
    path("delete/<int:product_id>/", views.delete, name="delete"),
    path("favorites/<int:product_id>/", views.favorites, name="favorites"),
    path("legal/", views.legal, name="legal"),
    path("myfavorites/", views.myfavorites, name="mesFavoris"),
    path("product/<int:product_id>/", views.product, name="product"),
    path("results/", views.results, name="results"),
    path("search/", views.search, name="search"),
    url(
        r"^product-autocomplete/$",
        ProductAutocomplete.as_view(),
        name="product-autocomplete",
    ),
]
