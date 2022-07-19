# Generated by Django 3.2 on 2022-07-12 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0010_auto_20220708_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='adults',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='booking',
            name='children',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='status',
            field=models.CharField(choices=[('propre', 'Propre'), ('sale', 'Sale'), ('nettoyage', 'Nettoyage')], default='propre', max_length=10),
        ),
    ]
