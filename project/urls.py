from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Xodim Api",
      default_version='v1.0',
      description="Test Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact"),

   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('app1.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)