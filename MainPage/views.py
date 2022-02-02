from django.shortcuts import render
from .models import About
# Create your views here.

def index_views(request):
    context={
        "deneme":about_text()
    }
    return render(request,'partials/indexblock.html',context)

def about_text():

    return About.objects.all()