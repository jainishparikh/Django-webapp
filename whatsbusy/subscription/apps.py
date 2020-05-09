from django.apps import AppConfig


class SubscriptionConfig(AppConfig):
    name = 'subscription'

    # triggering signales on events
    def ready(self):
        import subscription.signals
