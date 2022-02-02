from django.shortcuts import render

from .models import Category

# Create your views here.

def category_view(request):
    context={
        "category":Category.objects.all()
    }
    return render(request,'category.html',context)