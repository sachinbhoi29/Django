from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("planes",views.planes, name='planes'),
    path("helicopters",views.helicopters, name='helicopters'),
    path("cars",views.cars, name='cars'),
    path("others",views.others, name='others'),
    path("contact_us",views.contact_us, name='contact_us')
]
