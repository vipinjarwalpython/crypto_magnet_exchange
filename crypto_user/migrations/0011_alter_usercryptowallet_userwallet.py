# Generated by Django 4.2.8 on 2024-01-19 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_user', '0010_usercryptowallet_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercryptowallet',
            name='userwallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crypto_user.userwallet'),
        ),
    ]
