# Generated by Django 4.2.2 on 2023-06-19 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_address_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'A Propos'},
        ),
        migrations.AlterModelOptions(
            name='accreditation',
            options={'verbose_name_plural': 'Accreditation'},
        ),
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name_plural': 'Activités'},
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Adresse'},
        ),
        migrations.AlterModelOptions(
            name='collaborator',
            options={'verbose_name_plural': 'Collaborateur'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterModelOptions(
            name='hour',
            options={'verbose_name_plural': 'Horaires'},
        ),
        migrations.AlterModelOptions(
            name='members',
            options={'verbose_name_plural': 'Membres'},
        ),
        migrations.AlterModelOptions(
            name='possibility',
            options={'verbose_name_plural': 'Possibilités'},
        ),
        migrations.AlterModelOptions(
            name='price',
            options={'verbose_name_plural': 'Prix'},
        ),
        migrations.AlterModelOptions(
            name='query',
            options={'verbose_name_plural': 'Démandes'},
        ),
        migrations.AlterModelOptions(
            name='social',
            options={'verbose_name_plural': 'Réseau Sociaux'},
        ),
        migrations.AlterModelOptions(
            name='testimonial',
            options={'verbose_name_plural': 'Témoignages'},
        ),
        migrations.AlterModelOptions(
            name='vision',
            options={'verbose_name_plural': 'Visions'},
        ),
    ]