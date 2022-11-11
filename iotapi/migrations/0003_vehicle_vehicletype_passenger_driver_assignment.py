# Generated by Django 4.1.2 on 2022-11-01 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iotapi', '0002_coordinator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_vehicle', models.IntegerField(verbose_name='vehicle number ')),
                ('vehicle_type', models.IntegerField(verbose_name='Type vehicle')),
                ('vehicle_status', models.BooleanField(default=True, verbose_name='checked')),
                ('license_plate', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('passenger_code', models.CharField(blank=True, max_length=20)),
                ('passenger_permit', models.CharField(blank=True, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('user_modifer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='user_modifier_passenger', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('company_card', models.CharField(max_length=80)),
                ('drivers_license', models.CharField(max_length=15)),
                ('drivers_license_state', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('user_modifier', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='user_modifier_drive', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('state', models.BooleanField(default=True, verbose_name='checked')),
                ('conductor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='iotapi.driver')),
                ('user_modifier', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='user_modifier_assignment', to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='iotapi.vehicle')),
            ],
        ),
    ]
