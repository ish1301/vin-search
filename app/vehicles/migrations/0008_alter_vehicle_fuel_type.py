# Generated by Django 3.2.23 on 2024-01-23 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0007_alter_vehicle_exterior_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='fuel_type',
            field=models.CharField(max_length=100),
        ),
    ]
