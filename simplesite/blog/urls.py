from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    HomePageView,
    APIPlaygroundView,
    MachineLearningDemoView,
    register_request,
    BlogFeedView,
    BlogDetailView,
    BlogUpdateView,
    BlogCreateView,
    BlogDeleteView,
    GameView,
    AIView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("apiPlayground", APIPlaygroundView.as_view(), name="apiPlayground"),
    path("MLDemo", MachineLearningDemoView.as_view(), name="MLDemo"),
    path("accounts/register", register_request, name="register"),
    path("blogFeed", BlogFeedView.as_view(), name="blogFeed"),
    path('blogDetail/<slug:slug>/', BlogDetailView.as_view(), name='blogDetail'),
    path('blogDetail/<slug:slug>/update', BlogUpdateView.as_view(), name='blogUpdate'),
    path('blogDetail/<slug:slug>/delete', BlogDeleteView.as_view(), name='blogDelete'),
    path('blogCreate', BlogCreateView.as_view(), name='blogCreate'),
    path('game', GameView.as_view(), name='game'),
    path('AIDemo', AIView.as_view(), name='AIDemo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
