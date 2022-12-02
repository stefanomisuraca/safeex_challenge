from django.urls import path, include
from .lunarphase_view import LunarphaseView

urlpatterns = [
    path('lunarphase/', LunarphaseView.as_view())
]
