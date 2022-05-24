from django.forms import ModelForm
from rest_framework import serializers
from .models import Profil
from dj_rest_auth.serializers import UserDetailsSerializer


class ProfilSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer()
    class Meta:
        model = Profil
        fields = "__all__"
