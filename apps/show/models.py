from datetime import datetime
from django.db import models

# Create your models here.
class Email(models.Model):
    """emial记录"""

    email_code = models.CharField(max_length=10,verbose_name="随机编号",default="")
    email_body = models.CharField(max_length=1024,verbose_name="邮件内容",default="")
    email_title = models.CharField(max_length=20,verbose_name="邮件名",default="")
    email_from = models.CharField(max_length=30,verbose_name="发件人",default="")
    email_recv = models.CharField(max_length=30,verbose_name="收件人",default="")
    email_type = models.CharField(max_length=20,verbose_name="邮件类型",default="普通邮件")
    email_url = models.CharField(max_length=100,verbose_name="验证链接",default="")
    add_time = models.CharField(max_length=30,verbose_name="加入时间",default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        verbose_name = "email"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email_title

    @staticmethod
    def outputVcode(action_id):
        """输出连接参数指定的验证码"""
        vcodeR =  Email.objects.get(email_url__contains=action_id)
        vcode = vcodeR.email_code
        return vcode