from django.db import models

class Ips(models.Model):
    IPs = models.CharField(max_length=60)

class BannedIps(models.Model):
    bannedIPs = models.CharField(max_length=60)