from django.urls import path, include


from .views import (
    HomePageView,
    APIPlaygroundView,
    MachineLearningDemoView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("apiPlayground", APIPlaygroundView.as_view(), name="apiPlayground"),
    path("MLDemo", MachineLearningDemoView.as_view(), name="MLDemo")
]
