# Generated by Django 3.2.23 on 2024-01-23 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_alter_vehicle_dealer_vdp_last_seen_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='engine',
            field=models.CharField(max_length=255),
        ),
    ]
