from django.shortcuts import render

# Create your views here.

def book(request):
    name = request.POST["name"]
    email = request.POST["email"]
    phoneNumber = request.POST["phoneNumber"]
    message = request.POST["message"]
    selectPerson = request.POST["selectPerson"]
    date = request.POST["date"]
    time = request.POST["time"]
    print(request.POST)