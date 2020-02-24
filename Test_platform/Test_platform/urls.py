"""Test_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from user_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #用户应用
    path('hello/', views.say_hello),
    path('', views.index),#当不输路径的时候就会自动指向index
    path('index/', views.index),
    path('accounts/login/', views.index),
    path('logout/', views.logout),

    #项目管理
    path('project/', include('project_app.urls')),
    #模块管理
    path('module/', include('module_app.urls')),
    # 用例管理
    path('testcase/', include('testcase_app.urls')),

]
