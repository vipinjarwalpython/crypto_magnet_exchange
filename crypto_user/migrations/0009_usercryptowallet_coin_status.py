# Generated by Django 4.2.8 on 2024-01-19 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_user', '0008_alter_transaction_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercryptowallet',
            name='coin_status',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
