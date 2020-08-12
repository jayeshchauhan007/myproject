"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login-page/', views.loginpage, name='login-page'),
    path('registration-page/', views.registrationpage, name='registration-page'),
    path('register/', views.register, name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('edit-profile/',views.edit_profile,name='edit-profile'),
    path('update-profile/',views.update_profile,name='update-profile'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('send-otp/',views.send_otp,name='send-otp'),
    path('reset-password/',views.reset_password,name='reset-password'),
    path('recipes/',views.recipes,name='recipes'),
    path('about/',views.about,name='about'),
    path('recipe-single/',views.recipe_single,name='recipe-single'),
    path('contact/',views.contact,name='contact'),
    path('reviews/',views.reviews,name='reviews'),
    path('subscribe/',views.subscribe,name='subscribe'),
    path('send-comment/',views.send_comment,name='send-comment'),
    path('add-blog/',views.add_blog,name='add-blog'),
]
