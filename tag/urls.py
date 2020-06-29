from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newTag", views.newTag, name="newTag"),
    path("user/<str:username>", views.user, name="user")
]
