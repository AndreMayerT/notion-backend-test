from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TagView, ToolsViewSet

router = DefaultRouter()
router.register(r'tools', ToolsViewSet, basename='tools')

urlpatterns = [
    path('', include(router.urls)),
    path('tag=<str:tag>/', TagView.as_view()),
]
