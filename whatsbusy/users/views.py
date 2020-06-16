from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from subscription.models import Subscription
from movies.models import Movie
# Create your views here.


# main/index page
def index(request):
    if request.user.is_authenticated:
        return redirect('users:home')
    else:
        return render(request, 'index.html')


# registeration page
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            print("form invalid")
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

# home page
@login_required
def home(request):
    # subscription = Subscription.objects.get(user=request.user)
    movies = Movie.objects.all()
    context = {"movies": movies}
    return render(request, 'home.html', context)


@login_required
def account(request):
    subscription = Subscription.objects.get(user=request.user)
    context = {"user": request.user,
               "active": subscription.active, "trial": subscription.trial}
    return render(request, 'account_home.html', context)
