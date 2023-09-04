from django.shortcuts import render         #render = parcourir automatique le dossier dans templates
#from django.http import HttpResponse
from .models import Pizza
# Create your views here.

#/menu
def index(request):
    '''pizzas = Pizza.objects.all()
    pizzas_name_and_price = [pizza.nom +": " +str(pizza.prix)+ " Ariary" for pizza in pizzas]    #afficher les elements sur une ligne (mitambatra ni element)
    pizzas_name_str_and_price = " ,".join(pizzas_name_and_price)                                 #Faut separer par virgule   
    return HttpResponse("Les pizzas : "+ pizzas_name_str_and_price +".")'''
    
    pizzas = Pizza.objects.all().order_by('prix')      #Trier par Prix (alahatra araka ny prix) 
    return render(request, 'menu/index.html',{'pizzas': pizzas})