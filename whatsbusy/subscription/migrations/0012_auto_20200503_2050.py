# Generated by Django 2.2 on 2020-05-03 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0011_subscription_stripe_plan_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='stripe_token_id',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='stripe_plan_id',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='stripe_subscription_id',
            field=models.CharField(default='', max_length=50),
        ),
    ]
