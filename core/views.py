from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .models import Ips, BannedIps
from .webscraping import getIpsTorlist, getIpsOnionoo
from .forms import BanIpForm
from django.core.paginator import Paginator
from django.contrib import messages
# from rest_framework.response import Response
# from rest_framework import status
# from .api.serializers import BannedIpSerializer, IpSerializer

@api_view(['GET'])
def index(request):
    return render(request, 'home.html')

#endpoint 1: pegar todos os ips das redes externas e salvar em uma base de dados
@api_view(['GET'])
def list_all(request):    
    
    if getIpsTorlist():
        getIpsOnionoo()
    
    #serialized_ips = IpSerializer(ips, many=True)
    iplist = Ips.objects.all()
    ips_paginator = Paginator(iplist, 20)

    page_number = request.GET.get('page')
    page = ips_paginator.get_page(page_number)

    ipsList = {
        'page': page
    }
    
    return render(request, 'list_all.html', ipsList)
    #return Response(serialized_ips.data, status= status.HTTP_200_OK)


#endpoint 2: salvar os ips que o usuário não quer que apareçam no endpoint 3
@api_view(['GET', 'POST'])
def ban_ips(request):
    form = BanIpForm
    
    bannedList = getBanned()
    
    if (request.method == 'POST'):
        form = BanIpForm(request.POST)
        
        #banned = BannedIpSerializer(data= request.data)
        if form.is_valid():
            bannedIP= form.cleaned_data['IPs']
            if bannedIP not in bannedList:
                newBan = BannedIps(IPs = bannedIP)
                newBan.save()
                messages.success(request, 'IP banned successfully!')
                return redirect('home')
            else:
                messages.error(request, 'ERROR: IP already banned!')
                return render(request, 'ban_ips.html')
            #banned.save()
            #return Response(banned.data, status = status.HTTP_201_CREATED)
    
    return render(request, 'ban_ips.html')
    #return Response(banned.errors, status= status.HTTP_406_NOT_ACCEPTABLE)

#endpoint 3: retorna todos os ips salvos na base de dados, menos os que foram salvos pelo endpoint 2
@api_view(['GET'])
def list_unbanned(request):
    bannedList = getBanned()

    unbanned = (Ips.objects.exclude(IPs__in=bannedList).values())
    
    ips_paginator = Paginator(unbanned, 20)

    page_number = request.GET.get('page')
    page = ips_paginator.get_page(page_number)

    unbannedIps = {
        'page': page
    }
    #return Response({'unbanned': unbanned}, status= status.HTTP_200_OK)
    return render(request,'list_unbanned.html', unbannedIps)




def getBanned():

    banned = BannedIps.objects.all()

    bannedList= []
    [bannedList.append (k.IPs) for k in banned]
    
    return bannedList