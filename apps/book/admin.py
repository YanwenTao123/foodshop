from django.contrib import admin
from book.models import BookMsg,Foods

# Register your models here.

@admin.register(BookMsg)
class BookMsgAdmin(admin.ModelAdmin):
    list_display = ["book_sn","book_owner","email_booker","phone_booker","book_time","booker_nums","booker_msg","add_time"]
    fields = ["book_sn","book_owner","email_booker","phone_booker","book_time","booker_nums","booker_msg","add_time"]


@admin.register(Foods)
class Foods(admin.ModelAdmin):
    list_display = ["food_name","food_price","food_desc","food_class","food_img","food_kinds","is_show"]
    fields = ["food_name","food_price","food_desc","food_class","food_img","food_kinds","is_show"]
