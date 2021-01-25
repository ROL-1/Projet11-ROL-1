from django.conf.urls import url, include

from . import views

from .views import SignUpView

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^myaccount/", views.myaccount, name="myaccount"),
    url(r"^signup/", SignUpView.as_view(), name="signup"),
]
