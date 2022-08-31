from django.urls import path
from .views import index, ban_ips, list_all, list_unbanned


urlpatterns = [
    path('', index, name= 'home'),
    path('ban_ips/', ban_ips, name= 'ban_ips'),
    path('list', list_all, name= 'list_ips'),
    path('list_unbanned', list_unbanned, name= 'list_unbanned')
]
