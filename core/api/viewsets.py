from django.shortcuts import render
from rest_framework import viewsets
from ..models import Ips
from .serializers import IpSerializer


class IpsViewSet(viewsets.ModelViewSet):
    queryset = Ips.objects.all()
    serializer_class = IpSerializer


