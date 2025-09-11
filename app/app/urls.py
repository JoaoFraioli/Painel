from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    # Existing URL patterns
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    

    # Inclui as rotas do app empresa e do app endereco em /api/
    path('api/', include('empresa.urls')),
    path('api/', include('endereco.urls')),

    # API Token URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)