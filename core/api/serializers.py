from rest_framework import serializers
from ..models import Ips, BannedIps

class IpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ips
        fields = ['id', 'IPs']

class BannedIpSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannedIps
        fields = ['id', 'IPs']