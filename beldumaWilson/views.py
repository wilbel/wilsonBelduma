from django.http import HttpResponse
from django.shortcuts import render
from pais.models import Pais

def home(request):
    get_pais = Pais.objects.all()
    data = {
        'get_pais': get_pais
    }
    return render(request,'home.html',data)


