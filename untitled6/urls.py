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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r"^static/(?P<path>.*)$", serve, {"document_root": STATIC_ROOT}),
    url(r"^about/",about,name="about"),
    url(r"^index/",index,name="index"),
    url(r"^menu/",menu,name="menu"),
    url(r"^reservation/",reservation,name="reservation"),
    url(r"^team/",team,name="team"),
    url(r"^specail/",specail,name="specail"),
    url(r"^login/",login,name="login"),
    url(r"^phonelogin/",phonelogin,name="phonelogin"),
    url(r"^loginout",loginout,name="loginout"),
    url(r"^register/",register,name="register"),
    url(r"^personsetting/",personsetting,name="personsetting"),
    url(r"^leavemsg",leavemsg,name="leavemsg"),
    # url(r"^levelmsg",levelmsg,name="levelmsg"),

    #订单处理
    url(r'book/',book,name="bookHandler"),
    url(r"bookmanage/$",levelMsg1,name="bookmanage"),
    url(r"bookmanage.html",levelMsg1,name="bookmanage"),

    url(r"^robot/",chat,name="chat"),

    # 互亿验证码
    url(r"^huyi/",huyi,name="huyi"),
    url(r"^forgetpassword/",forgetpassword,name="forgetpassword"),
    url(r"^practice/",practice,name="practice")
]
