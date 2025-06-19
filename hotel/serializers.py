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
    room_details = serializers.SerializerMethodField()
    guest_details = serializers.SerializerMethodField()

    class Meta:
        fields = ["id",
        "reference",
        "checkIn",
        "checkOut",
        "status",
        "totalPrice",
        "guest",
        "guest_details",
        "adults",
        "children",
        "room",
        "room_details",
        "coupon",
        "recorded_by",
        "amountPaid",
        "amountDue",
        "created_at",
        "updated_at",
        "url"]
        model = Booking

    def get_room_details(self, obj):
        return {
            'number': obj.room.number,
            'type': obj.room.type.name
        }

    def get_guest_details(self, obj):
        return {
            'name': obj.guest.name,
            'firstname': obj.guest.firstname,
            'phone': obj.guest.phone
        }

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
    room_details = serializers.SerializerMethodField()
    guest_details = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = [
        "id",
        "reference",
        "checkIn",
        "checkOut",
        "status",
        "created_at",
        "updated_at",
        "guest",
        "guest_details",
        "room",
        "room_details",
        "recorded_by", 
        "url"
        ]

    def get_room_details(self, obj):
        return {
            'number': obj.room.number,
            'type': obj.room.type.name
        }

    def get_guest_details(self, obj):
        return {
            'name': obj.guest.name,
            'firstname': obj.guest.firstname,
            'phone': obj.guest.phone
        }

class DepenseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Depense


class PaymentSerializer(serializers.ModelSerializer):
    booking_details = serializers.SerializerMethodField()

    class Meta:
        fields = ['id', 'booking', 'booking_details', 'amount', 'status', 'type', 'created_at', 'updated_at']
        model = Payment

    def get_booking_details(self, obj):
        booking = obj.booking
        return {
            'reference': booking.reference,
            'guest_name': f"{booking.guest.name} {booking.guest.firstname}",
            'guest_phone': booking.guest.phone,
            'room_number': booking.room.number,
            'room_type': booking.room.type.name,
            'check_in': booking.checkIn,
            'check_out': booking.checkOut,
            'total_price': booking.totalPrice,
            'amount_paid': booking.amountPaid,
            'amount_due': booking.amountDue
        }


