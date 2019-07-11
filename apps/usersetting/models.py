from datetime import datetime
from django.db import models


# Create your models here.

class UserProfile(models.Model):
    """账号密码"""
    username = models.CharField(max_length=20,default="",unique=True,verbose_name="用户名")
    gender = models.CharField(max_length=10,default="男",verbose_name="性别")
    email = models.CharField(max_length=30,default="",verbose_name="邮箱")
    phone = models.CharField(max_length=11,default="",verbose_name="手机号")
    pwd = models.CharField(max_length=10,default="",verbose_name="密码")
    age = models.CharField(max_length=10,default="",verbose_name="年龄")
    add_time = models.CharField(max_length=30, default="0000-00-00 00:00:00", verbose_name="订单加入时间")

    class Meta:
        verbose_name = "账号管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    @staticmethod
    def inputPhone(phone):
        """输出手机号对应的username"""
        users = UserProfile.objects.get(phone=phone)
        return users.username

    @staticmethod
    def modifyUser(user,pwd):
        """修改个人设置"""

        userProfile = UserProfile.objects.get(username=user)
        userProfile.pwd = pwd
        userProfile.save()

    @staticmethod
    def register(user,pwd,age,email,phone,gender):
        """注册"""
        users = UserProfile(age=age,gender=gender,email=email,phone=phone,username=user,pwd=pwd,add_time=datetime.now().strftime('%Y-%m-%d'))
        users.save()


    @staticmethod
    def userInput():
        """输出用户列表"""
        users = UserProfile.objects.values_list("username")
        return users

    @staticmethod
    def pwdInput(user):
        """输出user对应密码"""
        pwd = ""
        try:
            userL = UserProfile.objects.get(username=user)
            pwd = UserProfile.objects.get(username=userL).pwd
        except:
            pwd = "账号密码错误"
        return pwd

    @staticmethod
    def pwdModify(phone,pwd):
        """修改手机号对应密码"""
        obj = UserProfile.objects.get(phone=phone)
        obj.pwd = pwd
        obj.save()


class UserManage(models.Model):
    """用户模块"""
    name = models.CharField(max_length=30,default="",verbose_name="模块名")
    website = models.CharField(max_length=50,default="",verbose_name="链接")
    add_time = models.CharField(max_length=30, default="0000-00-00 00:00:00", verbose_name="订单加入时间")

    class Meta:
        verbose_name = "用户模块"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    @staticmethod
    def allModdule():
        all = UserManage.objects.all()
        return all


class LeaveMsg(models.Model):
    """留言邮箱"""
    topic = models.CharField(max_length=30,verbose_name="主题",default="")
    email = models.CharField(max_length=30,verbose_name="邮箱名")
    add_time = models.CharField(max_length=30,verbose_name="加入时间",default=datetime.now().strftime("%Y-%m-%d"))

    class Meta:
        verbose_name = "留言邮箱"
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.email

    @staticmethod
    def saveMsg(email,topic):
        obj = LeaveMsg.objects.create(email=email,topic=topic,add_time=datetime.now().strftime("%Y-%m-%d"))

    @staticmethod
    def inputMsg():
        obj = LeaveMsg.objects.all()
        return obj
