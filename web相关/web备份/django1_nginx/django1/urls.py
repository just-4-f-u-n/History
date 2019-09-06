"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from app1 import views

urlpatterns = [
    path(r'',views.demo,name='demo'),
    path(r'app1/',views.home,name='home'),
    path(r'test1/',views.test1,name='test1'),
    path(r'data1/',views.data1,name='data1'), 
    #upload
    path(r'upfile/',views.upfile,name='upfile'),
    path('admin/', admin.site.urls),
]
