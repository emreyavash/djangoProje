
from . import views
from django.urls import path

urlpatterns = [
    path('categories',views.category_view,name='category'),
    path('categories/<slug:slug>',views.category_select,name='categorySlug'),
    path('course/<slug:slug>',views.course_detail,name='courseDetail'),
]
