from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
User = get_user_model()

class LunarphaseView(
    viewsets.ViewSet
):
    """
    Lunarphase view.

    * Requires basic authentication.

    """
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request):
        """
        Return a the current lunarphase.
        """
        
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
