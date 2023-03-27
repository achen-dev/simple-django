from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    HomePageView,
    APIPlaygroundView,
    MachineLearningDemoView,
    register_request,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("apiPlayground", APIPlaygroundView.as_view(), name="apiPlayground"),
    path("MLDemo", MachineLearningDemoView.as_view(), name="MLDemo"),
    path("accounts/register", register_request, name="register")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
