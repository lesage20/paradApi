from django.contrib import admin
from django.urls import path, include, re_path; re_path

from django.conf import settings
from django.conf.urls.static import static

# documentation de l'api
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Django template ",
      default_version='v1',
      description="Django template est un package qui vise a offrir les fonctionnailités de bases d'un site moderne via des api",
      contact=openapi.Contact(email="angezanou00@gmail.com"),
      license=openapi.License(name="BSD License"),
      author=openapi.License(name="Lesage"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('auth/profil/', include('userAccount.urls')),
    re_path(r'^api-docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^api-docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^api-redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
