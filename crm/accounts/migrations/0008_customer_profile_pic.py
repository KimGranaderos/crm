# Generated by Django 3.0.4 on 2020-03-11 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
