from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..moon_api import get_lunar_phase_service

from django.contrib.auth import get_user_model
User = get_user_model()

class LunarphaseViewSet(
    viewsets.ViewSet
):
    """
    Lunarphase view.

    * Requires basic authentication.

    """
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def list(self, request) -> Response:
        """
        Return a the current lunarphase.
        """
        return Response(get_lunar_phase_service())
