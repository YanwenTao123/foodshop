from django.http import JsonResponse
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from book.models import BookMsg,Foods
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
from plug.email import EmailHandler
from usersetting.models import UserManage, UserProfile
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


def passwordfind(request):
    """密码找回"""
    if request.method == "POST":
        return HttpResponse("DDD")
    else:
        return render(request,"email_phone_get.html")

def forgetpasswordemail(request):
    """忘记密码邮箱找回"""
    verify_code = request.session.get("random_str", "")
    if request.method == 'POST':  # 当提交表单时
        emailnum = request.POST.get("emailnum", "")
        verifycode = request.POST.get("verifycode", "")
        password = request.POST.get("password", "")
        password1 = request.POST.get("password1", "")
        print(verifycode, " = ", verify_code)

        if verify_code == verifycode:
            username1 = UserProfile.inputEmail(emailnum)
            if password == password1:
                UserProfile.pwdModifyByEmail(emailnum,password1)
                return HttpResponseRedirect("/index")
            else:
                return render(request, "emailfind.html", locals())
        else:
            return render(request, "emailfind.html", locals())
    else:
        return render(request, "emailfind.html", locals())

def passwordemail(request):
    """发单封验证码邮件"""
    title = "阿里offer"
    message = "恭喜您 成为我们公司CEO"
    email_from = "1241081280@qq.com"
    recs = ["m18867319705@163.com"]
    email_type = "普通邮件"
    #发送邮件
    if request.method == "POST":
      email_type = request.POST.get("email_type","")
    code = EmailHandler.send_register_email(email_title=title,email_body=message,email_from=email_from,email_recv=recs,email_type=email_type)
    request.session.set_expiry(60)
    request.session["random_str"] = code.get("code")
    # send_mail(title, message, email_from, recs)
    return JsonResponse({"result":"ok"})


