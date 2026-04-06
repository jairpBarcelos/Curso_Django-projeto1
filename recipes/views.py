from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'recipes/home.html', context={
        "nome": "Jair"
    })

def info(request):
    return render(request, 'recipes/info.html')

def contact(request):
    return HttpResponse("Contact")
