# Generated by Django 3.2 on 2023-09-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0011_auto_20230920_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='id_delivered_at',
            field=models.DateField(),
        ),
    ]