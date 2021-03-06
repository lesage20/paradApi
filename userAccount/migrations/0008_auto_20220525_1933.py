# Generated by Django 3.2 on 2022-05-25 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userAccount', '0007_alter_profil_idtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/usericon.png', upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='firstname',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profil',
            name='gender',
            field=models.CharField(choices=[('homme', 'Homme'), ('femme', 'Femme')], default='homme', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profil',
            name='idNumber',
            field=models.CharField(default='eoiuytred', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profil',
            name='idType',
            field=models.CharField(choices=[('cni', "Carte Nationale d'identité"), ('passeport', 'Passeport'), ('attestation', "Attestation d'identité")], default='cni', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profil',
            name='name',
            field=models.CharField(default='b', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profil',
            name='phone',
            field=models.CharField(default='n', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profil',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
