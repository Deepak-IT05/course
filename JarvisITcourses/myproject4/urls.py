"""myproject4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from myapp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
    path('result/',views.read,name='result'),
    path('insert/',views.insert,name='insert'),
    path('about/',views.about,name='about'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('index/',views.index,name='index'),
    path('service/',views.service,name='service'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('gallery/',views.gallery,name='gallery'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup_view,name='signup_view'),
    path('logout/',views.logout,name='logout')
]
