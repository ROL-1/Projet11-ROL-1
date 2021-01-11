from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^account/", views.account),
    url(r"^log/", views.log),
    url(r"^product/", views.product),
    url(r"^results/", views.results),
]
