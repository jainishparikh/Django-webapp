from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# User registartion form
# Modified and built upon Django default UserCreationForm and User object


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',
                  'password1', 'password2', )
