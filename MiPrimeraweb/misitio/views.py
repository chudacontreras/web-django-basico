from django.shortcuts import render
from django.http import HttpResponse
from .models import contacto

# Create your views here.

def index (request):
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