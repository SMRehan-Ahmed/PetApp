"""
URL configuration for pet_care project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from main.views import register, login_view , pet_profile , medicine_view , appointment_view , home , diet_plan

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('pet_profile/', pet_profile, name='pet_profile'),
    path('medicine/', medicine_view, name='medicine_view'),
    path('appointment/', appointment_view, name='appointment_view'),
    path('diet_plan/', diet_plan, name='diet_plan'),
    path('', login_view, name='login'),
    path('home/', home, name='home'),
]



