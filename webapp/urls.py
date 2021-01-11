from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^results/", views.results),
    url(r"^product/", views.product),
]