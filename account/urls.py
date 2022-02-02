
from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path("login",views.login_view,name="login"),
    path("register",views.register_view,name="register"),
    path("logout",views.logout_view,name="logout"),
    path("activate-user/<uidb64>/<token>",views.activate_view,name="activate"),
    path('change-password',views.change_password,name="changepassword"),
    path('change-password/<uidb64>/<token>',views.change_passwordlink,name="changepasswordlink"),
    path('change-password/<username>',views.forget_password,name="forgetpassword")
]
