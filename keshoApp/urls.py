# from enum import auto
from keshoApp  import views
from django.urls import path
#accessing the functionality of login in django to corresspond to line 14
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='indexpage'),
    path('about/',views.about,name='about'),
    path('babes/',views.AddBabe,name='AddBabe'),
    path('jumper/',views.jumper,name='jumper'),
    path('shops/',views.shops,name='shop'),
    path('home/',views.home,name='home'),
    path('payment/',views.AddPayment,name='AddPayment'),
    path('login/',auth_views.LoginView.as_view(template_name='keshoApp/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='keshoApp/logout.html'),name='logout'),
]