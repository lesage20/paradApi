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
      title="Paradisias ",
      default_version='1.0',
      description="Django template est un package qui vise a offrir les fonctionnailités de bases d'un site moderne via des api",
      contact=openapi.Contact(email="angezanou00@gmail.com"),
      author=openapi.License(name="Lesage"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('admin/', admin.site.urls),
   path('accounts/', include('userAccount.urls')),
   path('auth/registration/', include('dj_rest_auth.registration.urls')),
   path('auth/', include('dj_rest_auth.urls')),
   path('hotel/', include('hotel.urls')),
   re_path(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
