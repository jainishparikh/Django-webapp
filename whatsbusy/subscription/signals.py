from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Subscription
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings
import stripe


# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY

# Function to genarate customer id from STRIP on user registartion WhatsBusy using signals
@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, *args, **kwargs):
    print("inside post save")
    if created:

        user = User.objects.get(username=instance.username)
        new_customer_id = stripe.Customer.create(email=user.email)
        subscription = Subscription(
            user=user, stripe_customer_id=new_customer_id['id'])
        subscription.save()
