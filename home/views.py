from django.shortcuts import render, HttpResponse

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
    return render(requests, 'Contact_us.html')
