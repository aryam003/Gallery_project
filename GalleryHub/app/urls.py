from django.urls import path
from . import views

urlpatterns=[
    path('',views.user_login),
    path('logout',views.shop_logout),
    path('register',views.register),
    
    path('home',views.index),
    path('image',views.images),
    path('video',views.video),
    path('audio',views.audio),
    path('add_img',views.add_img),
    path('delete_img/<id>',views.delete_img),
    path('add_vdo',views.add_vdo),
    path('delete_vdo/<id>',views.delete_vdo),
    path('add_odo',views.add_odo),
    path('delete_odo/<id>',views.delete_odo),
    


]