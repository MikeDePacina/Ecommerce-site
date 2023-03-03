from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#request -> response
# views.py is a request handler

def say_hello(request):
    x = 2
    y = 3
    return render(request,'hello.html', {"member": "Gowon"})
