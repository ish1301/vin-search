# Generated by Django 3.2.23 on 2024-01-23 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0005_alter_vehicle_driven_wheels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='dealer_zip',
            field=models.CharField(max_length=10),
        ),
    ]
