"""
Definition of urls for pachong.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dianying/', views.dianying),
    path('pcdouban/', views.pcdouban),
    path('baidu/', views.baidu),
    path('pcjd/', views.pcjdshouji),
    path('jdshouji/', views.jdshouji),
]
