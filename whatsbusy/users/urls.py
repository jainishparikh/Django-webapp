from django.contrib import admin
from django.urls import include, path
from . import views

# namespace for users
app_name = "users"

urlpatterns = [
    # path to function rendering index page
    path('', views.index, name="index"),
    # path to function rendering Registration page
    path('register/', views.register, name="register"),
    # path to function rendering home page
    path('home/', views.home, name="home"),


]
