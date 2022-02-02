
from asyncio.windows_events import NULL
from django.shortcuts import redirect, render
from account.models import User,City

# Create your views here.
def userProfile_view(request,username):
    
    user = User.objects.get(username=username)
    if request.user.is_authenticated:
        if user.gender == 1:
            gender='Male'     
        elif user.gender==0:
            gender='Female'
        context={
            'gender':gender
        }
        if request.method == "POST":
            user.studentcertificate=request.FILES['studyCertificate']
            user.save()
            return render(request,"userprofile.html",context)
        return render(request,"userprofile.html",context)
    else:
        return redirect("login")
        
            
    

def profileEdit_view(request,username):
    user = User.objects.get(username=username)
    city = City.objects.all()
    selectedcity= City.objects.get(id = user.city_id)
    if request.method == "POST":
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.city = City.objects.get(id=request.POST['city'])
        user.gender = request.POST['gender']
        user.birthday = request.POST['birthday']
        user.userImage =request.FILES["images"] 

        user.save()
        return redirect('userprofile',username=username)

    return render(request,'profile-edit.html',{
        "city":city,
        "selectedcity":selectedcity
    })
    
def certificate_view(request):
    user = User.objects.filter(certificateverify=0).exclude(studentcertificate = "")
    context ={
        'user':user
    }
    
    return render(request,"usercertificate.html",context)
def certificateImage_view(request,username):
    user = User.objects.get(username=username)
    if request.method =="POST":
            
            if request.POST["button"] == "accept":
                user.certificateverify = 1
                user.save()
            elif request.POST['button'] == "reject":
                user.certificateverify = 0
                user.save()
            return redirect("certificate")
    return render(request,"certificateImage.html",{
        'user':user
    })