from django.contrib import admin
from .models import * 

# Register your models here.

admin.site.register(Floor)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(Coupon)
admin.site.register(Booking)