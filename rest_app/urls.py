from django.urls import include, path, re_path
from rest_app import views
from django.contrib import admin


urlpatterns = [
    path('', views.index)
]