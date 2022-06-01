from django.urls import path 
from . import views
from rest_framework.routers import SimpleRouter
routes = SimpleRouter()
routes.register('permissions', views.PermissionViewset)
routes.register('users', views.UserViewset)
routes.register('groups', views.GroupViewset)
routes.register('profiles', views.ProfilViewset)

urlpatterns = [
    path('', views.accounts),
    path('clients/', views.ClientViewset.as_view({'get': 'list', 'post': 'create'})),
    path('clients/<int:pk>', views.ClientViewset.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})),
    path('employes/', views.EmployeViewset.as_view({'get': 'list', 'post': 'create'})),
    path('employes/<int:pk>', views.EmployeViewset.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})),
]

urlpatterns += routes.urls

print(urlpatterns[0].resolve('clients/')) # 'name', 'pattern', 'resolve']