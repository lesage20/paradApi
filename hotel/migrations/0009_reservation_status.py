# Generated by Django 3.2 on 2022-07-02 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_remove_booking_roomtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('en attente', 'En attente'), ('payée', 'Payée'), ('archivée', 'Archivée')], default='en attente', max_length=15),
        ),
    ]
