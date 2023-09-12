from rest_framework import viewsets
from django_filters import rest_framework as filters
from .serializers import *
from rest_framework.permissions import DjangoModelPermissions

class FloorViewset(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = FloorSerializer
    queryset = Floor.objects.all().order_by('-created_at')
    
class RoomTypeViewset(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = RoomTypeSerializer
    queryset = RoomType.objects.all().order_by('-created_at')
    
class RoomViewset(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = RoomSerializer
    queryset = Room.objects.all().order_by('-created_at')
    filterset_fields = ['number', 'type']
    
class CouponViewset(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = CouponSerializer
    queryset = Coupon.objects.all().order_by('-created_at')


class BookingFilter(filters.FilterSet):
    checkIn_date = filters.DateTimeFilter(field_name="checkIn", lookup_expr="date__exact")
    checkOut_date = filters.DateTimeFilter(field_name="checkOut", lookup_expr="date__exact")
    class Meta:
        model = Booking
        fields = ['checkIn_date', 'checkOut_date']
        
        
class BookingViewset(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all().order_by('-created_at')
    filterset_class = BookingFilter

class FactureViewset(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = FactureSerializer
    queryset = Facture.objects.all().order_by('-created_at')
    # filterset_class = FactureFilter

class ReservationViewset(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
    # filterset_fields = ['guest', 'room', 'checkIn', 'checkOut', 'recorded_by' ]
    
    
   
class DepenseViewset(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = DepenseSerializer
    queryset = Depense.objects.all().order_by('-created_at')
    
