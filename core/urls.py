from django.contrib import admin
from django.urls import path, include
from .views import index, insert, unbanned

urlpatterns = [
    path('list', index, name="list-ips"),
    path('insert', insert, name= 'ban-ips'),
    path('unbanned', unbanned, name= 'unban-ips')
]