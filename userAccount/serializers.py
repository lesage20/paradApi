from django.forms import ModelForm
from rest_framework import serializers
from .models import Profil
from dj_rest_auth.serializers import UserDetailsSerializer
from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists, get_username_max_length
from allauth.account.adapter import get_adapter
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, Group, Permission
from django.core.exceptions import ValidationError as DjangoValidationError
from allauth.account.utils import setup_user_email

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"

class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    class Meta:
        model = User
        fields = ('id','url','username', "email", "groups", "profil")
        
class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = "__all__"



class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length = get_username_max_length(),
        min_length = allauth_settings.USERNAME_MIN_LENGTH,
        required = allauth_settings.USERNAME_REQUIRED,
    )
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    groups = serializers.CharField()
    def validate_groups(self, groups):
        try:
            group = Group.objects.get(name=groups)
        except Exception as exc:
            raise serializers.ValidationError(
                _("This role doesn't exists."),
                ) from exc
        return group
        
        
    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL and email and email_address_exists(email):
            raise serializers.ValidationError(
                _('A user is already registered with this e-mail address.'),
            )
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        self.group_name = self.validated_data.get('groups', '')
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        
        user = adapter.save_user(request, user, self, commit=False)
        print(f'user: {user}')
        if "password1" in self.cleaned_data:
            try:
                adapter.clean_password(self.cleaned_data['password1'], user=user)
            except DjangoValidationError as exc:
                raise serializers.ValidationError(detail=serializers.as_serializer_error(exc)) from exc

        user.save()
        user.groups.add(self.validate_groups(self.group_name))
        
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user
