# Generated by Django 2.1.7 on 2019-02-25 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_food_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='image',
        ),
    ]