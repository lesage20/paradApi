from django.urls import path 
from . import views
urlpatterns = [
    path('', views.ProfilListView.as_view(), name = "profile"),
    path('<int:pk>/', views.ProfilDetailView.as_view(), name = "profileDetail"),
]