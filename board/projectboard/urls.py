from django.urls import path
from projectboard import views

urlpatterns = [
    path("", views.projectboard, name="ProjectBoard"),
    path("title/", views.titlemethod, name="TitleMethod"),
]