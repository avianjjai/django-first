from django.contrib import admin
from django.urls import path
from . import views

app_name = "shorten"

urlpatterns = [
    path('',views.index,name = 'index'),
    path('add/',views.create,name = 'create'),
    path('<str:shortcode>/',views.goto,name = 'redirect'),
    path('edit/<int:pk>/',views.update,name = 'update'),
    path('delete/<int:pk>/',views.delete,name = 'delete')
]
