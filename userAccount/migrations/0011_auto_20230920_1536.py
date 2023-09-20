# Generated by Django 3.2 on 2023-09-20 15:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0010_alter_profil_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='domicile',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profil',
            name='father',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profil',
            name='id_delivered_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 20, 15, 36, 30, 116168)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profil',
            name='id_delivered_by',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profil',
            name='id_delivered_place',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profil',
            name='job',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profil',
            name='mother',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profil',
            name='nationnalite',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
