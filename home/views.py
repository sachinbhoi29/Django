from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.

def index(requests):
    context = {
    'key1':"Sachin is great",
    'key2':"Today is a beautiful day"
    }
    return render(requests, 'index.html',context)
    #return HttpResponse("This is the home page.")

def about(requests):
    return render(requests, 'About_us.html')

def planes(requests):
    return render(requests, 'Planes.html')

def helicopters(requests):
    return render(requests, 'Helicopters.html')

def cars(requests):
    return render(requests, 'Cars.html')

def others(requests):
    return render(requests, 'Others.html')

def contact_us(requests):
    if requests.method == "POST":
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        phone = requests.POST.get('phone')
        desc = requests.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
    return render(requests, 'Contact_us.html')
