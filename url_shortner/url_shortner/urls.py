from django.contrib import admin
from django.urls import path,include

from shorten.views import index,create,goto,update,delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shorten.urls'))
]
