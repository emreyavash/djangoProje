from django.urls import path
from . import views
urlpatterns = [
    path('user-profile/<username>',views.userProfile_view,name="userprofile"),
    path('profile-edit/<username>',views.profileEdit_view,name="profileEdit"),
    path('user-certificate',views.certificate_view,name="certificate"),
    path('certificate-image/<username>',views.certificateImage_view,name="certificateImage")
]
