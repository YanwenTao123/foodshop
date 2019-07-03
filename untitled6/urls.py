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
from django.views.static import serve
from untitled6.settings import STATIC_ROOT

from book.views import book

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^static/(?P<path>.*)$", serve, {"document_root": STATIC_ROOT}),
    url(r"^about/",about,name="about"),
    url(r"^index/",about,name="index"),
    url(r"^menu/",menu,name="menu"),
    url(r"^reservation/",reservation,name="reservation"),
    url(r"^team/",team,name="team"),
    url(r"^specail/",specail,name="specail"),

    #订单处理
    url(r'book/',book,name="bookHandler")
]
