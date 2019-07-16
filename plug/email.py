import string
import random
from datetime import datetime

from django.core.mail import send_mail
from untitled6.settings import EMAIL_FROM
from show.models import Email

class EmailHandler():
    """email发送处理"""

    @staticmethod
    def random_str(randomlenth=8):
        str_all = string.ascii_letters + string.digits
        send_str = random.sample(str_all, randomlenth)
        send_str = "".join(send_str)
        return send_str


    @staticmethod
    def send_register_email(email_title,email_body,email_from,email_recv, email_type="普通邮件"):
        # send_type = "register"
        email_record = Email()
        code = EmailHandler.random_str(8)
        url_random = EmailHandler.random_str(32)
        print("邮箱验证码：",code)
        #随机编码
        email_record.email_code = code
        email_record.email_title = email_title
        email_record.email_type = email_type
        email_record.email_body = email_body
        email_record.email_from = email_from
        email_record.email_recv = " ".join(email_recv)
        email_record.email_url = url_random
        email_record.add_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        email_record.save()
        if email_type == "forgetpassword":
            email_title = '登录密码找回链接'
            email_body = f"验证码:{code}"
            send_status = send_mail(email_title, email_body, EMAIL_FROM, email_recv)
            return {
                "code":code,
                "url_random":url_random
            }

        else:
            email_title = '注册激活链接'
            email_body = f"激活码:{code},\n请点击下面激活你的账号：http:localhost:8000/actionmail/{url_random}"
            send_status = send_mail(email_title, email_body, EMAIL_FROM, email_recv)
            return {
                "code":code,
                "url_random":url_random
            }