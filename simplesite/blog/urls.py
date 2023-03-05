from django.urls import path, include


from .views import (
    HomePageView,
    APIPlaygroundView
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("apiPlayground", APIPlaygroundView.as_view(), name="apiPlayground")
]