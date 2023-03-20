from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    HomePageView,
    APIPlaygroundView,
    MachineLearningDemoView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("apiPlayground", APIPlaygroundView.as_view(), name="apiPlayground"),
    path("MLDemo", MachineLearningDemoView.as_view(), name="MLDemo")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
