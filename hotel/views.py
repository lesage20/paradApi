from rest_framework import viewsets
from .serializers import *
from rest_framework.permissions import DjangoModelPermissions

class FloorViewset(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = FloorSerializer
    queryset = Floor.objects.all()
    
class RoomTypeViewset(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = RoomTypeSerializer
    queryset = RoomType.objects.all()
    
class RoomViewset(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    
class CouponViewset(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = CouponSerializer
    queryset = Coupon.objects.all()
    
class BookingViewset(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    
   
class DepenseViewset(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    serializer_class = DepenseSerializer
    queryset = Depense.objects.all()
    
