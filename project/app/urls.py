from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.jewelry, name='jewelry'),
    path('about/',views.about,name='about'),
    path('contactus/',views.contactus,name='contactus'),
    path('price/',views.price,name='price'),
    path('shop/',views.shop,name='shop'),
    path('shop1/',views.shop1,name='shop1'),
    path('registration/',views.registration,name='registration'),
    path('show_post/',views.show_post,name='show_post'),
    path('send/',views.send,name='send'),
    path('logout/', views.logout, name="logout"),
    path('login/', views.loginP, name="login"),
    path('register/', views.register, name="register"),
    
]