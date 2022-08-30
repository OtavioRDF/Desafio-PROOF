from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .models import Ips, BannedIps
from .webscraping import getIpsTorlist, getIpsOnionoo
from .forms import BanIpForm
from django.core.paginator import Paginator
# from rest_framework.response import Response
# from rest_framework import status
# from .api.serializers import BannedIpSerializer, IpSerializer

@api_view(['GET'])
def index(request):
    return render(request, 'home.html')

#endpoint 1: pegar todos os ips das redes externas e salvar em uma base de dados
@api_view(['GET'])
def list_all(request):    
    ips ={}
    
    if getIpsTorlist():
        getIpsOnionoo()
    
    ips["IP_list"] = Ips.objects.all()
    
    #serialized_ips = IpSerializer(ips, many=True)

    return render(request, 'list_all.html', ips)
    #return Response(serialized_ips.data, status= status.HTTP_200_OK)


#endpoint 2: salvar os ips que o usuário não quer que apareçam no endpoint 3
@api_view(['GET', 'POST'])
def ban_ips(request):
    form = BanIpForm

    if (request.method == 'POST'):
        form = BanIpForm(request.POST)
        
        #banned = BannedIpSerializer(data= request.data)
        if form.is_valid():
            bannedIP= form.cleaned_data['IPs']
            newBan = BannedIps(IPs = bannedIP)
            newBan.save()
            return redirect('home')
            #banned.save()
            #return Response(banned.data, status = status.HTTP_201_CREATED)
    
    return render(request, 'ban_ips.html')
    #return Response(banned.errors, status= status.HTTP_406_NOT_ACCEPTABLE)

#endpoint 3: retorna todos os ips salvos na base de dados, menos os que foram salvos pelo endpoint 2
@api_view(['GET'])
def list_unbanned(request):
    unbanned ={}
    banned = BannedIps.objects.all()

    bannedList= []
    [bannedList.append (k.IPs) for k in banned]
    
    unbanned["IP_list"] = (Ips.objects.exclude(IPs__in=bannedList).values())
    
    #return Response({'unbanned': unbanned}, status= status.HTTP_200_OK)
    return render(request,'list_unbanned.html', unbanned)


