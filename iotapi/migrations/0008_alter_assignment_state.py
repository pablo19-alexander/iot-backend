# Generated by Django 4.1.3 on 2022-12-01 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iotapi', '0007_device_devicevehicle_datadevice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='state',
            field=models.BooleanField(default=True),
        ),
    ]
