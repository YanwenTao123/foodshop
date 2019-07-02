from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"index.html")

def team(request):
    return render(request,"index.html")

def menu(request):
    return render(request,"index.html")

def specail(request):
    return render(request,"index.html")

def reservation(request):
    return render(request,"index.html")
