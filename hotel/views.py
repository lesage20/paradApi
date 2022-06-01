from rest_framework import viewsets
from .serializers import *

class FloorViewset(viewsets.ModelViewSet):
    serializer_class = FloorSerializer
    queryset = Floor.objects.all()
    
class RoomTypeViewset(viewsets.ModelViewSet):
    serializer_class = RoomTypeSerializer
    queryset = RoomType.objects.all()
    
class RoomViewset(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    
class CouponViewset(viewsets.ModelViewSet):
    serializer_class = CouponSerializer
    queryset = Coupon.objects.all()
    
class BookingViewset(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    
   
class DepenseViewset(viewsets.ModelViewSet):
    serializer_class = DepenseSerializer
    queryset = Depense.objects.all()
    
