# Generated by Django 4.2.2 on 2023-07-01 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0005_alter_price_levels'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='level',
            table='level',
        ),
        migrations.AlterModelTable(
            name='price',
            table='price',
        ),
    ]