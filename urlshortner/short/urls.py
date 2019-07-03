from django.urls import path,include
from . import views

app_name = "short"

urlpatterns = [
    
    path('',views.index,name = 'index'),
    path('signup/',views.signup,name = 'signup'),
    path('signin/',views.signin,name = 'signin'),
    path('logout/',views.user_logout,name = 'logout'),
    path('shorturl/',views.shorturl,name = 'shorturl'),
    path('<int:id>/detail/',views.detail,name = 'detail'),
    path('<str:shortcode>/',views.goto,name = 'redirect'),
    path('<int:id>/delete/',views.delete,name = 'delete'),
]
