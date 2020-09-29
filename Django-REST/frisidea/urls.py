"""Urls module."""
from django.conf import settings
from django.urls import include, path, re_path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

from frisidea.views.api import user as user_api
from frisidea.views.api import auth as auth_api


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'users', user_api.UserViewSet)


urlpatterns = [
    # API
    path('v1/', include((router.urls, 'api_views'), )),
    path('v1/auth/login', auth_api.LoginView.as_view(), name='api_login'),
    path('v1/api-token-auth/', obtain_auth_token, name='api_token_auth'),
]