# Generated by Django 3.1.4 on 2021-05-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.IntegerField(default=123456789),
        ),
    ]
