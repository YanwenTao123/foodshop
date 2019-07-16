"""untitled6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from show.views import *
from usersetting.views import *
from django.views.static import serve
# from untitled6.settings import STATIC_ROOT
from book.views import book
from pay.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r"^static/(?P<path>.*)$", serve, {"document_root": STATIC_ROOT}),

    # 导航栏链接处理
    url(r"^about/",about,name="about"),
    url(r"^index/",index,name="index"),
    url(r"^menu/",menu,name="menu"),
    url(r"^reservation/",reservation,name="reservation"),
    url(r"^team/",team,name="team"),
    url(r"^specail/",specail,name="specail"),

    # 个人设置
    url(r"^personsetting/",personsetting,name="personsetting"),

    # 留言设置
    url(r"^leavemsg",leavemsg,name="leavemsg"),
    # url(r"^levelmsg",levelmsg,name="levelmsg"),

    # 登录注册
    url(r"^loginout", loginout, name="loginout"),
    url(r"^register/", register, name="register"),
    url(r"^login/",login,name="login"),
    url(r"^phonelogin/",phonelogin,name="phonelogin"),
    url(r"passwordfind",passwordfind,name="passwordfind"),
    url(r"^forgetpasswordemail/",forgetpasswordemail,name="forgetpasswordemail"),
    url(r"emailfind/",passwordemail,name="passwordemail"),


    #订单处理
    url(r'book/',book,name="bookHandler"),
    url(r"bookmanage/$",levelMsg1,name="bookmanage"),
    url(r"bookmanage.html",levelMsg1,name="bookmanage"),

    # 客服（对接图灵机器人）
    url(r"^robot/",chat,name="chat"),

    # 互亿验证码
    url(r"^huyi/",huyi,name="huyi"),
    url(r"^forgetpassword/",forgetpassword,name="forgetpassword"),
    url(r"^practice/",practice,name="practice"),

    # 邮箱
    url(r"email/",send_my_mail,name="send_my_mail"),
    url(r"actionmail/$",actionmail1,name="actionmail1"),
    url(r"^actionmail/(?P<action_id>[0-9a-zA-Z]+)",actionmail,name="actionmail"),

    # 支付
    url(r'^page1/', page1),
    url(r'^payindex/', payindex),
	url(r'^page2/', page2),
]
