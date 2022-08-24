from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Ips, BannedIps
from .api.serializers import BannedIpSerializer, IpSerializer
from .webscraping import getIpsTorlist, getIpsOnionoo

#endpoint 1: pegar todos os ips das redes externas e salvar em uma base de dados
@api_view(['GET'])
def index(request):    
    if getIpsTorlist():
        getIpsOnionoo()
    
    ips = Ips.objects.all()
    serialized_ips = IpSerializer(ips, many=True)

    return Response(serialized_ips.data, status= status.HTTP_200_OK)

#endpoint 2: salvar os ips que o usuário não quer que apareçam no endpoint 3
@api_view(['POST'])
def insert(request):
    banned = BannedIpSerializer(data= request.data)
    if banned.is_valid():
        banned.save()
        return Response(status = status.HTTP_201_CREATED)
    
    return Response(banned.errors, status= status.HTTP_204_NO_CONTENT)


#endpoint 3: retorna todos os ips salvos na base de dados, menos os que foram salvos pelo endpoint 2
@api_view(['GET'])
def unbanned(request):
    banned = BannedIps.objects.all()

    unbanned = []
    [unbanned.append (k.bannedIPs) for k in banned]
    
    difference = (Ips.objects.exclude(IPs__in=unbanned).values())
    
    serialized_unban = IpSerializer(difference, many=True)

    return Response(serialized_unban.data, status= status.HTTP_200_OK)




