from dataclasses import field
from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Profil
from .serializers import *
from dj_rest_auth.registration.app_settings import RegisterSerializer, register_permission_classes
from django.conf import settings
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework import status
from allauth.account import app_settings as allauth_settings
from allauth.account.utils import complete_signup, send_email_confirmation
from allauth.account.views import ConfirmEmailView
from allauth.utils import email_address_exists, get_username_max_length
from dj_rest_auth.models import TokenModel
from dj_rest_auth.app_settings import (
    JWTSerializer, TokenSerializer, create_token,
)
from dj_rest_auth.utils import jwt_encode
from django.contrib.auth.models import Group, Permission, User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import urls
sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters('password1', 'password2'),
)


# serializers go here
class ProfilViewset(viewsets.ModelViewSet):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer

class ClientViewset(viewsets.ModelViewSet):
    clientsGroup = Group.objects.filter(name='client').values_list('pk', flat=True)
    users = User.objects.filter(groups__in=list(clientsGroup)).values_list('pk', flat=True)
    queryset = Profil.objects.filter(user_id__in=list(users))
    serializer_class = ProfilSerializer

class EmployeViewset(viewsets.ModelViewSet):
    clientsGroup = Group.objects.exclude(name='client').exclude(name='admin').values_list('pk', flat=True)
    users = User.objects.filter(groups__in=list(clientsGroup)).values_list('pk', flat=True)
    queryset = Profil.objects.filter(user_id__in=list(users))
    serializer_class = ProfilSerializer


class PermissionViewset(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    
class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = register_permission_classes()
    token_model = TokenModel
    throttle_scope = 'dj_rest_auth'

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_response_data(self, user):
        if allauth_settings.EMAIL_VERIFICATION == \
                allauth_settings.EmailVerificationMethod.MANDATORY:
            return {'detail': _('Verification e-mail sent.')}

        if getattr(settings, 'REST_USE_JWT', False):
            data = {
                'user': user,
                'access_token': self.access_token,
                'refresh_token': self.refresh_token,
            }
            return JWTSerializer(data, context=self.get_serializer_context()).data
        elif getattr(settings, 'REST_SESSION_LOGIN', False):
            return None
        else:
            return TokenSerializer(user.auth_token, context=self.get_serializer_context()).data

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers,) if (data := self.get_response_data(user)) else Response(status=status.HTTP_204_NO_CONTENT, headers=headers)

    def perform_create(self, serializer):
        print(dir(serializer))
        user = serializer.save(self.request)
        if allauth_settings.EMAIL_VERIFICATION != \
                allauth_settings.EmailVerificationMethod.MANDATORY:
            if getattr(settings, 'REST_USE_JWT', False):
                self.access_token, self.refresh_token = jwt_encode(user)
            elif not getattr(settings, 'REST_SESSION_LOGIN', False):
                # Session authentication isn't active either, so this has to be
                #  token authentication
                create_token(self.token_model, user, serializer)

        complete_signup(
            self.request._request, user,
            allauth_settings.EMAIL_VERIFICATION,
            None,
        )
        return user

@api_view(('GET',))
def accounts(request):
    url_list = urls.urlpatterns
    host = request._request.get_host()
    data = {}
    for url in url_list:
        pat = str(url.pattern).split('/')
        if 1 < len(pat) < 3 and pat[1] in ['$', '']:
            data[pat[0].strip('^')] = f"http{'s' if request._request.is_secure() else ''}://{host}/" + pat[0].strip('^')
    return Response(data)