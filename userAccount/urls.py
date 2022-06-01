from django.urls import path 
from . import views
from rest_framework.routers import DefaultRouter
routes = DefaultRouter()
routes.register('profiles', views.ProfilViewset)
routes.register('permissions', views.PermissionViewset)
routes.register('users', views.UserViewset)
routes.register('groups', views.GroupViewset)
routes.register('clients', views.ClientViewset)
routes.register('employes', views.EmployeViewset)

urlpatterns = [
    path('registration/', views.RegisterView.as_view())
]

urlpatterns += routes.urls