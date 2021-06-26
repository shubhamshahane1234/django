from django.http.response import HttpResponse
from django.shortcuts import render
from home.models import Contact

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        phone = request.POST.get('phone')
        contact = Contact(name=name,surname=surname,phone=phone)
        contact.save()
   
        
    return render(request,'contact.html')
