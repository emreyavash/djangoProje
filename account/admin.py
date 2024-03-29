from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,City
# Register your models here.
class CityAdmin(admin.ModelAdmin):
    list_display=("cityName",)

class UserConfig(UserAdmin):
    list_display=("email","username","first_name","last_name","is_active","is_staff","genderName","birthday",)
    search_fields = ("email","user_name","first_name",)
    def genderName(self,obj):
        html = ""
        if obj.gender == "1":
            html+="Male"
        else:
            html+="Female"

        return html
    fieldsets = [
        ("Kullancı Bilgileri", {'fields': ['first_name']}),   
        (None, {'fields': ['last_name']}),
        (None, {'fields': ['email']}),   
        (None, {'fields': ['username']}),
        (None, {'fields': ['password']}),   
        (None, {'fields': ['userImage']}),   
        (None, {'fields': ['birthday']}),
        (None, {'fields': ['gender']}),   
        ("Yetki Bilgileri", {'fields': ['is_superuser']}),   
        (None, {'fields': ['is_active']}),
        (None, {'fields': ['is_staff']}),   
        ("Zaman Bilgileri", {'fields': ['date_joined']}),   
        
        (None, {'fields': ['last_login']}),   
    ]
admin.site.register(User,UserConfig)
admin.site.register(City,CityAdmin)
