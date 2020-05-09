# Generated by Django 2.2 on 2020-05-03 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0013_remove_subscription_stripe_plan_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='stripe_customer_id',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='stripe_token_id',
            field=models.CharField(default='', max_length=50),
        ),
    ]