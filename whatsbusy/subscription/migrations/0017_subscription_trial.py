# Generated by Django 2.2 on 2020-05-03 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0016_auto_20200503_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='trial',
            field=models.BooleanField(default=False),
        ),
    ]
