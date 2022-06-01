from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from .models import *

class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Floor

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = RoomType

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Room
        

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Coupon

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Booking

class DepenseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Depense


