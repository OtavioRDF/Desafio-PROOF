from dataclasses import field, fields
from pyexpat import model
from .models import BannedIps
from django.forms import ModelForm
from django import forms


class BanIpForm(ModelForm):
    class Meta:
        model = BannedIps
        fields = '__all__'