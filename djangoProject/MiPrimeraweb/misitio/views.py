from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import contacto
import requests
import json
# Create your views here.

def index (request):
    if request.method == 'POST':
        nombre = request.POST.get('fname')
        apellido = request.POST.get('lname')
        
        r = requests.get('http://api.icndb.com/jokes/random?firstName='+ nombre +'&amp&lastName='+ apellido)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')
        
        context = { 'joke': joke }
        # print(joke)
        # print(json_data) 
        # print(r.text)
        # print (nombre)
        # print (apellido)
        return render(request, 'misitio/index.html', context)
    else:
        return render(request, 'misitio/index.html')
        
    
def portfolio (request):
    return render(request, 'misitio/portfolio.html')

def contact (request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')
        c = contacto(Email = email_r, Subject = subject_r, Message = message_r) 
        c.save()
        return render(request, 'misitio/agradecimiento.html')
    else:
        return render(request, 'misitio/contact.html')
    
    # return render(request, 'misitio/contact.html')