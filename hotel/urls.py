from rest_framework.routers import DefaultRouter
from .views import *
routes = DefaultRouter()
routes.register('etages', FloorViewset)
routes.register('types_chambre', RoomTypeViewset)
routes.register('chambres', RoomViewset)
routes.register('coupons', CouponViewset)
routes.register('locations', BookingViewset)
routes.register('depenses', DepenseViewset)

urlpatterns = routes.urls
