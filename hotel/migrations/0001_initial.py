# Generated by Django 3.2 on 2022-05-24 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userAccount', '0007_alter_profil_idtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('discount', models.IntegerField(default=0)),
                ('code', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Coupon',
                'verbose_name_plural': 'Coupons',
            },
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('number', models.IntegerField(unique=True)),
                ('status', models.CharField(choices=[('actif', 'Actif'), ('inactif', 'Inactif')], max_length=7)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Etage',
                'verbose_name_plural': 'Etages',
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('numberAdult', models.IntegerField(default=1)),
                ('numberChildren', models.IntegerField(default=0)),
                ('price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Type de Chambre',
                'verbose_name_plural': 'Type de Chambres',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='hotel.floor')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='hotel.roomtype')),
            ],
            options={
                'verbose_name': 'Chambre',
                'verbose_name_plural': 'Chambres',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=50, null=True)),
                ('checkIn', models.DateField()),
                ('checkOut', models.DateField()),
                ('status', models.CharField(choices=[('attente', 'Attente'), ('payée', 'Payée'), ('archivée', 'Archivée')], max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='hotel.coupon')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings_guest', to='userAccount.profil')),
                ('recorded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings_recorder', to='userAccount.profil')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='hotel.room')),
                ('roomType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='hotel.roomtype')),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
    ]
