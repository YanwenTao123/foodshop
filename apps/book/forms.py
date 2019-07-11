from django import forms
from django.forms import widgets


class Form1(forms.Form):
    """login"""
    username = forms.CharField()
    password = forms.CharField()


class Form2(forms.Form):
    """register"""
    username = forms.CharField()
    password = forms.CharField()

class Form3(forms.Form):
    """个人信息修改"""
    username = forms.CharField()
    password = forms.CharField()