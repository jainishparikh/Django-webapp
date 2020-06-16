from django.contrib import admin
from django.urls import include, path
from . import views

# namespace for users
app_name = "movies"

urlpatterns = [
    # path to function rendering index page
    path('get/<str:movie>', views.get_movie, name="get_movie"),


]
