from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from subscription.models import Subscription
# Create your views here.


# main/index page
def index(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
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
    subscription = Subscription.objects.get(user=request.user)
    context = {"active": subscription.active, "trial": subscription.trial}
    return render(request, 'home.html', context)
