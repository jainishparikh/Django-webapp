from django.urls import include, path
from . import views

# namespace for subscriptions
app_name = "subscription"

urlpatterns = [
    # path to function rendering page to get premium subscription
    path('premium/', views.getPremium,
         name="getPremium"),
    # path to function interacting with STRIPE apis for premium subscription
    path('pay/', views.registerPremium,
         name="registerPremium"),
    # path to function to cancel premium subscription
    path('cancel/', views.cancelPremium,
         name="cancelPremium"),

]
