import requests
from .models import Ips

#Cabeçalho para fazer requisição usando requests
header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36'}


# Pega os ips das redes externas e as salva na mesma base de dados
def getIpsTorlist():
    request = requests.get('https://www.dan.me.uk/torlist/', headers= header)
    
    if request.status_code == 403:
        return False
    else:
        cleanDataBase = Ips.objects.all()
        cleanDataBase.delete()         
        
        request = request.text

        results =[]
        results.append(request.split('\n'))
        
        try:
            for i in results:
                ips = Ips(IPs= i)
                ips.save()
                print(request)
        except:
            return True

        return True



def getIpsOnionoo():
    request = requests.get('https://onionoo.torproject.org/summary?limit=5000', headers= header)
    data_request = request.json()
    results = [item['a'][0] for item in data_request["relays"] if 'a' in item and item['a']]
    
    for i in results:
        if(Ips.objects.filter(IPs=i).exists() == False):
            ips = Ips(IPs= i)
            ips.save()
    
