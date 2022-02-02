from django.contrib import admin

from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=("categoryName",)
admin.site.register(Category,CategoryAdmin)