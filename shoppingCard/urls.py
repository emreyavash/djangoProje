from django.urls import path
from . import views
urlpatterns = [
    path("<str:username>",views.shoppingCart_view,name="shoppingCart"),
    path("<str:username>",views.shopping,name="shopping"),
    # path("<str:username>",views.shoppingbyuser,name="shoppingbyuser"),
]

