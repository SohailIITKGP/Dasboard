from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JsondataViewSet

router = DefaultRouter()
router.register(r'jsondata', JsondataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
