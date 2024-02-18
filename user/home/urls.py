from django.urls import path

from . import views
app_name="home"
urlpatterns = [
    path('',views.home,name="home"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('confirm/',views.confirm_reg,name="confirm"),
    path('checkout/',views.checkout,name="checkout"),
    path('generate/',views.generatePDF,name="generate"),
]
