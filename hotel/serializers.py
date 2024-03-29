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
        fields = ["id",
        "reference",
        "checkIn",
        "checkOut",
        "status",
        "totalPrice",
        "guest",
        "adults",
        "children",
        "room",
        "coupon",
        "recorded_by",
        "payment",
        "created_at",
        "updated_at",
        "url"]
        model = Booking
        
class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id",
        "booking",
        "status",
        "amount",
        "created_at",
        "updated_at",
        "url"]
        model = Facture
        
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = fields = [
        "id",
        "reference",
        "checkIn",
        "checkOut",
        "status",
        "created_at",
        "updated_at",
        "guest",
        "room",
        "recorded_by", 
        "url"
        ]
        

class DepenseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Depense


