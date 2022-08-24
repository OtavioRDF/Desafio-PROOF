from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api import viewsets as ipsviewsets

router = routers.DefaultRouter()
router.register(r'ips', ipsviewsets.IpsViewSet, basename="ips")

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
