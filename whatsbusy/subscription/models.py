from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Subscription model with OnetoOne relationship with the User


class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    trial = models.BooleanField(default=False)
    stripe_customer_id = models.CharField(max_length=500, default='')
    stripe_token_id = models.CharField(max_length=500, default='')
    stripe_subscription_id = models.CharField(max_length=500, default='')
