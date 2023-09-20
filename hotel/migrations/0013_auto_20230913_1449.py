# Generated by Django 3.2 on 2023-09-13 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_auto_20230823_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('pj', 'Payé jour'), ('dj', 'Dette jour'), ('dt', 'Dette totale'), ('dp', 'Dette payée'), ('archive', 'Archivée')], max_length=15),
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('status', models.CharField(choices=[('pj', 'Payé jour'), ('dj', 'Dette jour'), ('dt', 'Dette totale'), ('dp', 'Dette payée'), ('archive', 'Archivée')], max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factures', to='hotel.booking')),
            ],
            options={
                'verbose_name': 'depense',
                'verbose_name_plural': 'depenses',
            },
        ),
    ]