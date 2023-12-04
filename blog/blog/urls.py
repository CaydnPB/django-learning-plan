from django.contrib import admin
from django.urls import path
from .views import post_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', post_list, name='post_list'),
]