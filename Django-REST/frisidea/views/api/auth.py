"""User views."""
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response

from frisidea.serializers.user import UserSerializer

User = get_user_model()


class LoginView(APIView):
    permission_classes = (IsAuthenticated,)             

    def get(self, request):
        content = {'message': 'You are logged in !'}
        return Response(content)