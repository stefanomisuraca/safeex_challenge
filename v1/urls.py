from django.urls import path, include
from rest_framework import routers
from v1 import views as api_views

router = routers.DefaultRouter()
router.register(r'test', api_views.LunarphaseView, basename="lunarphase")

urlpatterns = [
    path('', include(router.urls))
]
