import time

from datetime import datetime
from django.shortcuts import render, redirect
from book.models import BookMsg,Foods

# Create your views here.

def book(request):
    if request.method == "POST":
        data = {}
        print(type(request.POST["name"]),request.POST["name"])
        print(type(request.POST["phoneNumber"]),request.POST["phoneNumber"])
        print(type(request.POST["email"]),request.POST["email"])
        print(type(request.POST["message"]),request.POST["message"])
        print(type(request.POST["date"]+" "+ request.POST["time"]),request.POST["date"]+" "+ request.POST["time"])
        print(type(datetime.now),datetime.now)
        print(type(request.POST["selectPerson"]),request.POST["selectPerson"])
        data["book_sn"] = int(round(time.time() * 1000))
        data["book_owner"] = request.POST["name"]
        data["email_booker"] = request.POST["email"]
        data["phone_booker"] = request.POST["phoneNumber"]
        data["booker_msg"] = request.POST["message"]
        data["booker_nums"] = int(request.POST["selectPerson"])
        data["book_time"] = request.POST["date"]+" "+ request.POST["time"]
        data["add_time"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        BookMsg.objects.create(**data)
        # book_owner, email_booker, phone_booker, book_time, booker_nums, booker_msg =\
        #     request.POST["name"],request.POST["email"],request.POST["phoneNumber"],request.POST["message"],request.POST["selectPerson"],request.POST["date"]+" "+ request.POST["time"]
        return redirect("/index")


