# Generated by Django 3.1.4 on 2021-05-12 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210511_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(max_length=300, upload_to='productimg'),
        ),
    ]
