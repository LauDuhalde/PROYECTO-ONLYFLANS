"""
URL configuration for onlyflans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from web.views import index, about, welcome, contact, success,logout_page, signup, signup_success
from web import views
app_name = 'web'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('about', about, name="about"),
    path('welcome', welcome, name="welcome"),
    path('contact', contact, name="contact"),
    path('success', success, name="success"),
    path('accounts/', include('django.contrib.auth.urls')),  
    path('logout_page', logout_page, name="logout_page"),
    path('flan/<int:flan_id>/', views.flanDetail, name='flanDetail'),
    path('accounts/signup', signup, name='signup'),
    path('signup_success', signup_success, name="signup_success"),
]
