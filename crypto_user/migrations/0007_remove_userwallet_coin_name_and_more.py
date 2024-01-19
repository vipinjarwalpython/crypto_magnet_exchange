# Generated by Django 4.2.8 on 2024-01-19 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_user', '0006_userwallet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userwallet',
            name='coin_name',
        ),
        migrations.RemoveField(
            model_name='userwallet',
            name='coin_price',
        ),
        migrations.RemoveField(
            model_name='userwallet',
            name='coin_quantity',
        ),
        migrations.CreateModel(
            name='UserCryptoWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('coin_name', models.CharField(max_length=100)),
                ('coin_quantity', models.DecimalField(decimal_places=2, max_digits=15)),
                ('coin_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('userwallet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crypto_user.userwallet')),
            ],
        ),
    ]
