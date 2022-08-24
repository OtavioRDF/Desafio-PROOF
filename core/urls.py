from django.urls import path
from .views import index, insert, unbanned


urlpatterns = [
    path('list', index, name='list-ips'),
    path('insert', insert, name= 'ban-ips'),
    path('list-unbanned', unbanned, name= 'unbanned-ips')
]
