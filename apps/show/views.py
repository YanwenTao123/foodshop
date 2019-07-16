import datetime
import json
import random

import requests
from django.core.mail import send_mass_mail, send_mail
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext

from book.models import Foods,BookMsg,ChatMsg
from usersetting.models import UserProfile, UserManage, LeaveMsg
from book.forms import Form1, Form2, Form3
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse

from untitled6.settings import TULING_API,API_KEY,USER_ID,APIID,APIKEY
from show.models import Email
from plug.email import EmailHandler


# Create your views here.

def index(request):
    username = request.session.get("username","")
    if username:
        breakfast = Foods.food("0")
        lunch = Foods.food("1")
        dinner = Foods.food("2")
        food_class = ["breakfast","lunch","dinner"]
        foods = {"breakfast":breakfast,
                 "lunch":lunch,
                 "dinner":dinner
                 }
        specail_food = Foods.specail()
        user_module = UserManage.allModdule()
        return render(request,"index.html",locals())
    else:
        return HttpResponseRedirect("/login/")
    # return render(request,"index.html",locals())

def about(request):
    user_module = UserManage.allModdule()
    username = request.session.get("username", "")
    if username:
        user_module = UserManage.allModdule()
        breakfast = Foods.food("0")
        lunch = Foods.food("1")
        dinner = Foods.food("2")
        food_class = ["breakfast", "lunch", "dinner"]
        foods = {"breakfast": breakfast,
                 "lunch": lunch,
                 "dinner": dinner
                 }
        specail_food = Foods.specail()
        return render(request,"about.html",locals())
    else:
        return HttpResponseRedirect("/login/")

def team(request):
    user_module = UserManage.allModdule()
    username = request.session.get("username", "")
    if username:
        user_module = UserManage.allModdule()
        breakfast = Foods.food("0")
        lunch = Foods.food("1")
        dinner = Foods.food("2")
        food_class = ["breakfast", "lunch", "dinner"]
        foods = {"breakfast": breakfast,
                 "lunch": lunch,
                 "dinner": dinner
                 }
        specail_food = Foods.specail()
        return render(request,"team.html",locals())
    else:
        return HttpResponseRedirect("/login/")

def menu(request):
    user_module = UserManage.allModdule()
    username = request.session.get("username", "")
    if username:
        user_module = UserManage.allModdule()
        breakfast = Foods.food("0")
        lunch = Foods.food("1")
        dinner = Foods.food("2")
        food_class = ["breakfast", "lunch", "dinner"]
        foods = {"breakfast": breakfast,
                 "lunch": lunch,
                 "dinner": dinner
                 }
        specail_food = Foods.specail()
        return render(request,"menu.html",locals())
    else:
        return HttpResponseRedirect("/login/")

def specail(request):
    user_module = UserManage.allModdule()
    username = request.session.get("username", "")
    if username:
        user_module = UserManage.allModdule()
        breakfast = Foods.food("0")
        lunch = Foods.food("1")
        dinner = Foods.food("2")
        food_class = ["breakfast", "lunch", "dinner"]
        foods = {"breakfast": breakfast,
                 "lunch": lunch,
                 "dinner": dinner
                 }
        specail_food = Foods.specail()
        return render(request,"special-dishes.html",locals())
    else:
        return HttpResponseRedirect("/login/")

def reservation(request):
    user_module = UserManage.allModdule()
    username = request.session.get("username", "")
    if username:
        user_module = UserManage.allModdule()
        breakfast = Foods.food("0")
        lunch = Foods.food("1")
        dinner = Foods.food("2")
        food_class = ["breakfast", "lunch", "dinner"]
        foods = {"breakfast": breakfast,
                 "lunch": lunch,
                 "dinner": dinner
                 }
        specail_food = Foods.specail()
        return render(request,"reservation.html",locals())
    else:
        return HttpResponseRedirect("/login/")

def login(request):
    username = ""
    if request.method == 'POST':  # 当提交表单时
        form = Form1(request.POST)  # form 包含提交的数据
        if form.is_valid():  # 如果提交的数据合法
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            if (username,) in list(UserProfile.userInput()):
                if (pwd == UserProfile.pwdInput(username)):
                    # return render(request,"index.html",locals())
                    # req = redirect("/index")
                    # req.set_cookie("username",username)
                    # req.set_cookie("pwd",pwd)
                    # return req
                    request.session.set_expiry(12000)
                    request.session["username"] = username
                    return HttpResponseRedirect("/index")
                else:
                    pwdd = "账号密码错误"
                    return render(request, "login.html", locals())
            else:
                pwdd = UserProfile.pwdInput(username)
                return render(request, "login.html", locals())
    else:  # 当正常访问时
        form = Form1()
    return render(request,"login.html",locals())

def phonelogin(request):
    username1 = ""
    verify_code = request.session.get("verify_code","")
    if request.method == 'POST':  # 当提交表单时
        phone = request.POST.get("phone","")
        verifycode = request.POST.get("verifycode","")
        print(verifycode," ",verify_code)
        if verify_code == verifycode:
            username1 = UserProfile.inputPhone(phone)
            print(username1,"--")
            request.session.set_expiry(12000)
            request.session["username"] = username1
            return HttpResponseRedirect("/index")
        else:
            return render(request, "phonelogin.html", locals())
    else:
        return render(request,"phonelogin.html",locals())

def forgetpassword(request):
    """忘记密码"""
    username1 = ""
    verify_code = request.session.get("verify_code", "")
    if request.method == 'POST':  # 当提交表单时
        phone = request.POST.get("phone", "")
        verifycode = request.POST.get("verifycode", "")
        password = request.POST.get("password", "")
        password1 = request.POST.get("password1", "")
        print(verifycode, " ", verify_code)
        if verify_code == verifycode:
            username1 = UserProfile.inputPhone(phone)
            if password == password1:
                UserProfile.pwdModify(phone,password1)
                return HttpResponseRedirect("/index")
            else:
                return render(request, "forgetpassword.html", locals())
        else:
            return render(request, "forgetpassword.html", locals())
    else:
        return render(request, "forgetpassword.html", locals())

def huyi(request):
    """短信验证码"""
    # 用户名 查看用户名请登录用户中心->验证码、通知短信->帐户及签名设置->APIID
    account = APIID
    # 密码 查看密码请登录用户中心->验证码、通知短信->帐户及签名设置->APIKEY
    password = APIKEY
    mobile = "18867319705"
    msg_code = ""
    for i in range(6):
        k = random.randint(0, 9)
        msg_code = msg_code +  str(k)
    text = "您的验证码是：{}。请不要把验证码泄露给其他人。".format(msg_code)
    request.session.set_expiry(20)
    request.session["verify_code"] = msg_code
    print(text)
    data = {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'}
    response = requests.post(url='http://106.ihuyi.com/webservice/sms.php?method=Submit', data=data)
    print(data)
    return HttpResponse(json.dumps({"result":"ok"}), content_type='application/json')
    # return JsonResponse({"result":"ok"})

def leavemsg(request):
    """留言邮箱"""
    user_module = UserManage.allModdule()
    username = request.session.get("username","")
    allMsg = LeaveMsg.inputMsg()
    if username:
        email = request.POST.get("leavemsg","")
        topic = request.POST.get("topic","")
        print(email)
        strLen = len(email)
        is_at = True if "@" in email else False
        is_com = True if "com" in email else False
        print(strLen)
        print(is_com)
        print(is_at)
        if strLen > 8 and is_at and is_com:
            LeaveMsg.saveMsg(email,topic)
        return render(request,"levelmsg.html",locals())
    else:
        return HttpResponseRedirect("/index")

def loginout(request):
    """注销"""
    del request.session['username']
    return HttpResponseRedirect("/login/")

def personsetting(request):
    """个人信息修改"""
    user_module = UserManage.allModdule()
    username = request.session.get("username","")
    if username:
        if request.method == "POST":
            # form = Form3(request.POST)
            # if form.is_valid():
            #     username = form.cleaned_data["username"]
            #     pwd = form.cleaned_data["password"]
            #     UserProfile.modifyUser(username,pwd)
            username = request.POST.get("username","")
            password1 = request.POST.get("password","")
            print(request.POST)
            UserProfile.modifyUser(username,password1)
            return HttpResponseRedirect("/personsetting/")
            # else:
            #     return HttpResponseRedirect("/personsetting/")
        else:
            form = Form3()
        return render(request,"personSetting.html",locals())
    else:
        form = Form3()
        return HttpResponseRedirect("/login/")

def register(request):
    user_module = UserManage.allModdule()
    if request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        gender = request.POST.get("gender","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        age = request.POST.get("age","")
        UserProfile.register(username,password,age,email,phone,gender)
        return HttpResponseRedirect("/login")
    else:
        form = Form2()
    return render(request,"register.html",locals())

def chat(request):
    username = request.session.get("username", "")
    if username:
        if request.method == "POST":
            msg = request.POST.get("msg","")
            from_who = username
            to_who = "Resto"
            ChatMsg.addMsg(msg,from_who,to_who)
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
            }
            data ={
                "reqType": 0,
                "perception": {
                    "inputText": {
                        "text": msg
                    },
                    "selfInfo": {
                        "location": {
                            "city": "深圳",
                            "province": "广东",
                            "street": "信息路"
                        }
                    }
                },
                "userInfo": {
                    "apiKey": API_KEY,
                    "userId": USER_ID
                }
            }
            data = json.dumps(data).encode('utf8')
            response = requests.post(url=TULING_API,data=data,headers=headers).json()
            print(response)
            from_who_r = "Resto"
            to_who_r = username
            msg_r = response.get("results","")
            if msg_r:
                print(type(msg_r[0].get("values").get("text")),)
                msg_r = msg_r[0].get("values").get("text")
                if msg_r == "请求次数超限制!":
                    msg_r = "我在休息了"
            else:
                msg_r = "我在休息了"
            ChatMsg.addMsg(msg_r, from_who_r, to_who_r)
            allMsg = list(ChatMsg.objects.all())[-10:]
            print(allMsg)
            return render(request,"chat.html",locals())
        else:
            allMsg = list(ChatMsg.objects.all())[-10:]
            return  render(request,"chat.html",locals())
    else:
        return HttpResponseRedirect("/login")

def practice(request):
    """测试"""
    username = UserProfile.inputPhone("16620064525")
    print(type(username))
    return HttpResponse(username)

def send_my_mail(request):
    """发单封验证码邮件"""
    title = "阿里offer"
    message = "恭喜您 成为我们公司CEO"
    email_from = "1241081280@qq.com"
    recs = ["m18867319705@163.com"]
    email_type = "普通邮件"
    #发送邮件
    # if request.method == "POST":
    #   email_type = request.POST.get("email_type","")
    random_url = EmailHandler.send_register_email(email_title=title,email_body=message,email_from=email_from,email_recv=recs,email_type=email_type).get("random_url")
    request.session.set_expiry(60)
    request.session["random_str"] = random_url
    # send_mail(title, message, email_from, recs)
    return HttpResponseRedirect("/actionmail/")
    # return render(request,"actionform.html",locals())

# 多封普通邮件的发送
def send_emailss(req):
    title1 = "腾讯offer"
    message1 = "恭喜您 被骗了"
    email_from = "1625211623@qq.com"
    title2 = "这是一封挑事的邮件"
    message2 = "大哥大哥别杀我"
    recs1 = ["17694871425@163.com",
            "569677884@qq.com",
            "ichenyouzhi@163.com"]
    recs2 = ["17694871425@163.com",
             "569677884@qq.com",
             "ichenyouzhi@163.com",
             "m18742863100@163.com"]
    senders1 = (title1, message1, email_from, recs1)
    senders2 = (title2, message2, email_from, recs2)
    send_mass_mail((senders1, senders2), fail_silently=False)
    return HttpResponse("OK")

def actionmail(request,action_id):
    """邮件验证码验证处理"""
    if request.method == "POST":
        print('request.session.get("random_str",""):',request.session.get("random_str",""))
        if request.session.get("random_str",""):
            v_code = request.POST.get("action","")
            vcode = Email.outputVcode(action_id)
            if vcode == v_code:
                return  HttpResponse("验证成功")
            else:
                return HttpResponse("验证失败")
    else:
        return HttpResponseRedirect("/actionmail/")

def actionmail1(request):
     random_str = request.session.get("random_str","")
     print("random_str:",random_str)
     return render(request,"actionform.html",locals())


