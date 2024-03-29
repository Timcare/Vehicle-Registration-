from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #path('',views.base,name="base"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('register/', views.RegisterForm.as_view(), name="register"),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
    path('password_change/',auth_views.PasswordChangeView.as_view(),name="password_change"),
    path('password_change/form',auth_views.PasswordChangeDoneView.as_view(),name="password_change_done"),
    path('profile/',views.Profile,name="profile"),
    path('license/',views.License,name="license"),
]
