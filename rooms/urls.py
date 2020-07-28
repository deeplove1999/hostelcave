from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('Room/', views.Room,name="Room"),
    path('aboutus/' , views.aboutus,name="aboutus"),
    path('contactus/', views.contactus,name="contactus"),
    path('contactform/',views.contactform,name="contactform"),
]