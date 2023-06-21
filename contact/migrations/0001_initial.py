# Generated by Django 4.2.2 on 2023-06-21 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(blank=True, max_length=250)),
                ('phone', models.CharField(blank=True, max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Les Contacts des temoignants Clients',
            },
        ),
        migrations.CreateModel(
            name='ContactHelp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': "Les Supports d'Aide client (Contact)",
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Les Posts Clients pour AHSM',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('network_name', models.CharField(max_length=200)),
                ('social_type', models.CharField(choices=[('fab fa-linkedin-in', 'LinkedIn'), ('fab fa-twitter', 'Twitter'), ('fab fa-facebook-f', 'Facebook'), ('fab fa-instagram', 'Instagram')], max_length=25)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Les Réseaux Sociaux AHSM',
            },
        ),
    ]
