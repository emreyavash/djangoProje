from django.shortcuts import redirect, render,get_list_or_404
from .models import Shopping
from account.models import User
from category.models import Courses,Teacher

# Create your views here.

def shoppingCart_view(request,username):
    if request.user.is_authenticated:
        user = User.objects.get(username=username) 
        # shoppingUser = Shopping.objects.filter(user = user.id)
        shopping(request,username)
        shopping1 = get_list_or_404(Shopping,user=user.id)
        
        context={
            "product": shopping1,
            }
        return render(request,"shoppingPage.html",context)

        # if shopping.exists():
        #     context={
        #     "product": shopping
        #     }
        #     return render(request,"shoppingPage.html",context)
        # else:
        #     return render(request,"shoppingPage.html",{
        #         "error":"Shopping Cart is empty."
        #     })
        
    return render(request,"index.html")

def shopping(request,username):
    if request.method == "POST":
        user=User.objects.get(username=username)
        total_price = request.POST["coursePrice"]
        quantity = request.POST["quantity"]
        course=Courses.objects.get(courseName = request.POST["courseName"])
        product_id = course.id
        user_id = user.id
        teacher = Teacher.objects.get(teacherName=request.POST["teacherName"]).id
        shop = Shopping.objects.create(total_price=total_price,quantity=quantity,product_id=product_id,user_id=user_id,teacher_id=teacher)
        shop.save()
        return redirect('category')
    return render(request,"index.html")

# def shoppingbyuser(request,username):
#     user = User.objects.get(username=username)
#     shoppingUser = Shopping.objects.get(user_id = user.id)
#     if shoppingUser.exits():
#         context={
#             "product": Shopping.objects.all()
#         }
#         return render(request,"shoppingPage.html",context)
#     else:
#         return render(request,"shoppingPage.html",{
#             "error":"Shopping Cart is empty."
#         })
    