# Generated by Django 4.2.8 on 2024-01-22 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_user', '0011_alter_usercryptowallet_userwallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercryptowallet',
            name='profitandloss',
            field=models.FloatField(default=0.0),
        ),
    ]
