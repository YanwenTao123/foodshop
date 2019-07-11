from django.contrib import admin
from usersetting.models import UserProfile,UserManage
# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["username","pwd","add_time"]
    fields = ["username","pwd","add_time"]

@admin.register(UserManage)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["name","website","add_time"]
    fields = ["name","website","add_time"]

