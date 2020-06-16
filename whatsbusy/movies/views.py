from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from subscription.models import Subscription
from .models import Movie

# Create your views here.
@login_required
def get_movie(request, movie):
    subscription = Subscription.objects.get(user=request.user)
    movieObj = Movie.objects.get(name=movie)
    context = {"user": request.user,
               "active": subscription.active, "movie": movieObj}
    print(context["active"])
    return render(request, "movie.html", context)
