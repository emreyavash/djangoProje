from django.shortcuts import redirect, render

from .models import Category,Courses
from account.models import User
from shoppingCard.models import Shopping

# Create your views here.
def category_select(request,slug):
    context={
        "course":Category.objects.get(slug=slug).courses_set.filter(is_active=True),
        # "course":Courses.objects.filter(category__slug=slug),
        "category":Category.objects.all(),
        "selected_category":slug
    }
    return render(request,"category.html",context)

def category_view(request):
    context={
        "category":Category.objects.all(),
        "course":Courses.objects.all(),
        
    }
    return render(request,'category.html',context)

def course_detail(request,slug):
    context={
        "course":Courses.objects.get(slug=slug),
        
    }
    return render(request,"courseDetail.html",context)
    
