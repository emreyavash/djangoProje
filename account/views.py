from django.shortcuts import redirect, render
from .models import User,City
# from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import authenticate,login,logout
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.core.mail import EmailMessage,send_mail
from django.contrib.sites.shortcuts import get_current_site
from .utils import generate_token
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
from django.conf import settings
# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        username = request.POST.get('username')
        password= request.POST.get('password')
    
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.emailverify:

                login(request,user)
                return redirect('home')
            else:
                return render(request,"login.html",{
                    'error':'Email kutunuzu kontrol ediniz.'
                })
        return render(request,'login.html',{
        'error':'Şifre Yanlış',
        
        })
    return render(request,"login.html")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    context={
            'city':City.objects.all()
            }
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        username=request.POST['username']
        repassword = request.POST['repassword']
        email = request.POST['email']
        gender = request.POST['gender']
        city = request.POST['city']
        birthday = request.POST['birthday']
        tc = request.POST['tc']
        phone = request.POST['phone']
        if password == repassword:
            
            if User.objects.filter(email=email).exists():
                 return render(request,"register.html",{
                'error':"email is used",
                "first_name":first_name,
                'last_name':last_name,
                'username':username,
                'gender':gender,
                'city':city,
                'birthday':birthday,
                'tc':tc,
                'phone':phone,
                'city':City.objects.all()
            })
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password,gender=gender,city=city,birthday=birthday,tc=tc,phone=phone)
                user.save()

                current_site=get_current_site(request)
                send_mail(
                    'Activate Your Account',
                    render_to_string("activate.html",{
                        "user":user, 
                        "domain":current_site,
                        "uid":urlsafe_base64_encode(force_bytes(user.id)),
                        "token":generate_token.make_token(user)
                    }),
                    settings.DEFAULT_FROM_EMAIL,
                    [user.email],
                    fail_silently=False,
                )

                return redirect('home')
        else:
            return render(request,"register.html",{
                'error':"Password doesn't macth",
                "first_name":first_name,
                'last_name':last_name,
                'email':email,
                'gender':gender,
                'username':username,
                'city':city,
                'birthday':birthday,
                'tc':tc,
                'phone':phone,
                'city':City.objects.all()

            })
    
    return render(request,"register.html",context)

def logout_view(request):
    logout(request)
    return redirect('home')


def activate_view(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
        token=generate_token.make_token(user)
    except Exception as e:
        user=None
    if user and generate_token.check_token(user,token):
        user.emailverify = True
        user.save()

        return redirect("login")
    return render(request,"account/activate_failed.html",{
        "user":user
    })

def change_password(request):
    if request.method == "POST":
        email = request.POST["email"]
        user = User.objects.get(email=email)
        if user.email==email:
            current_site=get_current_site(request)
            send_mail(
                'Change Your Password',
                render_to_string("forgetpasswordlink.html",{
                    "user":user, 
                    "domain":current_site,
                    "uid":urlsafe_base64_encode(force_bytes(user.id)),
                    "token":generate_token.make_token(user)
                }),
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
            return redirect("home")
        else:
            return render(request,"forgetpassword.html",{
                "error":"Email is wrong"
            })
    return render(request,"forgetpassword.html")


def change_passwordlink(request,uidb64,token):
   
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
        token=generate_token.make_token(user)
    except Exception as e:
        user=None
    if user and generate_token.check_token(user,token):
        username = user.username
        return redirect("forgetpassword",username=username)
    return render(request,"forgetpassword.html")

def forget_password(request,username):
    if request.method == "POST":
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        if password == repassword:
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            return redirect("login")
        else:
            return render(request,"forgetpasswordtemp.html",{
                "error":"Password doesn't match"
            })
    return render(request,"forgetpasswordtemp.html")