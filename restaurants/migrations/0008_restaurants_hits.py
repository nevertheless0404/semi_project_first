# Generated by Django 3.2.13 on 2022-11-04 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_alter_restaurants_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='hits',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
