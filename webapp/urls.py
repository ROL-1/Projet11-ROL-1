from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^contact/", views.contact, name="contact"),
    url(r"^legal/", views.legal, name="legal"),
    url(r"^product/", views.product, name="product"),
    url(r"^results/", views.results, name="results"),
    url(r"^save/", views.save, name="save"),  # <str:product_id>
    url(r"^search/", views.search, name="search"),
]
