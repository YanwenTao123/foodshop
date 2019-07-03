from datetime import datetime
from django.db import models
import time

# Create your models here.

class BookMsg(models.Model):
    """订单信息"""
    book_sn = models.PositiveIntegerField(default=time.struct_time,verbose_name="订单号",unique=True)
    book_owner = models.CharField(max_length=30,default="",verbose_name="订单主人")
    email_booker = models.EmailField(max_length=50,default="",verbose_name="联系邮箱")
    phone_booker = models.CharField(max_length=20,default="",verbose_name="联系电话")
    book_time = models.DateTimeField(default="",verbose_name="预定时间")
    booker_nums = models.PositiveIntegerField(default=0, verbose_name="预订人数")
    booker_msg = models.TextField(default="", verbose_name="留言信息")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="订单加入时间")

    class Meta:
        verbose_name = "订单信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book_sn


class Foods(models.Model):
    """food信息"""
    FOOD_KINGS = [
        ("0","早餐"),
        ("1","中餐"),
        ("2","晚餐"),
    ]
    IS_SHOW = [
        (False,"否"),
        (True,"是"),
    ]
    FOOD_TYPE = [
        ("0","轮播图"),
        ("1","Special"),
        ("2",""),
    ]
    food_name = models.CharField(default="",max_length=30,verbose_name="食物名")
    food_price = models.CharField(default="",max_length=10,verbose_name="食物价格")
    food_desc = models.TextField(default="",verbose_name="食物描述")
    food_class = models.CharField(choices=FOOD_KINGS,verbose_name="早中晚餐",default="0",max_length=10)
    food_img = models.CharField(max_length=300,verbose_name="图片地址")
    food_kinds = models.CharField(choices=FOOD_TYPE,default="2",verbose_name="食物类型",max_length=10)
    is_show = models.BooleanField(default=True,choices=IS_SHOW,verbose_name="是否展示")

    class Meta:
        verbose_name = "food信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.food_name