"""safeex_project URL Configuration """

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/', include('v1.api_views.urls')),
    path('fe/', include('v1.fe_views.urls'))
]
