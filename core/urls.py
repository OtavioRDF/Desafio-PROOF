from django.urls import path
from .views import index, insert, unbanned


urlpatterns = [
    path('list', index, name='list-ips'),
    path('ban-ips', insert, name= 'ban-ips'),
    path('list-unbanned', unbanned, name= 'unbanned-ips')
]
