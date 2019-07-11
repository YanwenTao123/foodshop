from django.shortcuts import render,HttpResponseRedirect
from book.models import BookMsg,Foods
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
from usersetting.models import UserManage
from plug.CustomPaginator import CustomPaginator

def levelMsg1(request):
    """分页控制"""
    specail_food = Foods.specail()
    user_module = UserManage.allModdule()
    username = request.session.get("username","")
    print(username)
    if username:
        current_page = request.GET.get("p","")
        if current_page == "":
            current_page = 1
        current_page = int(current_page)
        book_list = BookMsg.objects.filter(username=username)
        book_paginator = CustomPaginator(current_page,3,book_list,3)
        book_page = book_paginator.page(current_page)
        return render(request,"bookmanage.html",locals())
    else:
        return HttpResponseRedirect("/login")



