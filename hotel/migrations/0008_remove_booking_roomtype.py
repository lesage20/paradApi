# Generated by Django 3.2 on 2022-06-30 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_reservation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='roomType',
        ),
    ]
