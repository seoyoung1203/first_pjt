"""
URL configuration for first_pjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# first_app 폴더 내부의 views.py
from first_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('hello/', views.hello),
    path('lunch/', views.lunch),
    path('lotto/', views.lotto), 
    # variable routing
    path('profile/<username>/', views.profile),
    path('cube/<int:number>/', views.cube),
    path('articles/', views.articles),

    # path('news/', view.news)

    # 빈도화지
    path('ping/', views.ping),
    # 사람들이 입력한 경로
    path('pong/', views.pong),
]
