from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente

# Create your views here.
def home(request):
    return render(request, 'agenda.html')

def pacientes(request):
    #if request.method == "GET":
      return render(request, 'clientes.html')
    #elif request.method  == "POST":
       

      # nome = request.POST.get('nome')

      # cliente = Cliente(
        #  nome = nome
       #)

       #cliente.save
       
       