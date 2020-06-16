from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Subscription
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.conf import settings
from .models import Subscription
from users import views
import stripe


# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.

# rendering form to get premium
@login_required
def getPremium(request):
    return render(request, 'checkout.html')

# interecting with STRIPE apis to get premium subscription
@login_required
def registerPremium(request):
    subscription_obj = Subscription.objects.get(user=request.user)
    customer_id = subscription_obj.stripe_customer_id
    card_token = request.POST['stripeToken']

    # saving card with the customer
    saveCard(subscription_obj, card_token, customer_id)

    # generating charge
    charge = chargeCustomer(customer_id)

    # Setting up subscription
    subscription_obj = subscribeCustomer(subscription_obj, customer_id)

    subscription_obj.active = True
    trial = subscription_obj.trial
    subscription_obj.save()
    context = {"active": True, "trial": trial}
    return redirect('users:home')


# cancel subscription
@login_required
def cancelPremium(request):
    subscription_obj = Subscription.objects.get(user=request.user)
    subscription_id = subscription_obj.stripe_subscription_id
    stripe_subscription = stripe.Subscription.delete(subscription_id)
    subscription_obj.active = False
    trial = subscription_obj.trial
    subscription_obj.save()
    context = {"active": False, "trial": trial}
    return redirect('users:home')


# link card with customer
def saveCard(subscription, card_token, customer_id):
    if subscription.stripe_token_id == "":
        subscription.stripe_token_id = card_token

        customer = stripe.Customer.modify(
            customer_id,
            source=card_token
        )


# charge customer
def chargeCustomer(customer_id):
    charge = stripe.Charge.create(
        customer=customer_id,
        amount=4999,
        currency='usd'

    )
    return charge


# subscribe a customer
def subscribeCustomer(subscription, customer_id):
    if subscription.active == False and subscription.trial == False:
        stripe_subscription = stripe.Subscription.create(
            customer=customer_id,
            items=[
                {
                    'plan': 'plan_HCy6UA9z08gVnb',
                },
            ],
            trial_period_days=7,
        )
        subscription.stripe_subscription_id = stripe_subscription["id"]
        subscription.trial = True
    else:
        stripe_subscription = stripe.Subscription.create(
            customer=customer_id,
            items=[
                {
                    'plan': 'plan_HCy6UA9z08gVnb',
                },
            ],
        )
        subscription.stripe_subscription_id = stripe_subscription["id"]
    return subscription
