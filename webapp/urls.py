from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^account/", views.account),
    url(r"^contact/", views.contact),
    url(r"^legal/", views.legal),
    url(r"^log/", views.log),
    url(r"^product/", views.product),
    url(r"^results/", views.results),
]
