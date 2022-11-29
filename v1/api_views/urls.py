from django.urls import path, include
from rest_framework import routers
from .lunarphase import LunarphaseViewSet

router = routers.DefaultRouter()
router.register(r'test', LunarphaseViewSet, basename="lunarphase")

urlpatterns = [
    path('', include(router.urls))
]
