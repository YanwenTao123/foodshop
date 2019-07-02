from datetime import datetime
from django.db import models

# Create your models here.

class BookMsg(models.Model):
    """订单信息"""
    book_sn = models.PositiveIntegerField(default=0,verbose_name="订单号",unique=True)
    book_owner = models.CharField(max_length=30,default="",verbose_name="订单主人")
    email_booker = models.EmailField(max_length=50,default="",verbose_name="联系邮箱")
    phone_booker = models.CharField(max_length=20,default="",verbose_name="联系电话")
    book_time = models.DateTimeField(default="",verbose_name="预定时间")
    booker_nums = models.PositiveIntegerField(default=0, verbose_name="预订人数")
    booker_msg = models.TextField(default="", verbose_name="留言信息")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="订单加入时间")

    class Mate:
        verbose_name = "订单信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book_sn
