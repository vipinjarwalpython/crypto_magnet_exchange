# Generated by Django 4.2.8 on 2024-01-29 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_user', '0021_rename_ammount_fundtransactions_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateCoinDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_price', models.FloatField(default=0.0)),
                ('profitandloss', models.FloatField(default=0.0)),
                ('coin_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crypto_user.usercryptowallet')),
                ('userwallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crypto_user.userwallet')),
            ],
        ),
    ]
