# Generated by Django 4.2.2 on 2023-07-01 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_alter_about_options_alter_aboutahsm_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutitti',
            options={'verbose_name_plural': 'Les Informations sur ITTI'},
        ),
        migrations.AlterModelTable(
            name='aboutitti',
            table='about_itti',
        ),
    ]