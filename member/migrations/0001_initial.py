# Generated by Django 4.2.2 on 2023-06-21 04:17

import Web.utils
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accreditation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.FileField(default='', null=True, upload_to=Web.utils.upload_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif', 'jpeg', 'webp', 'svg', 'bmp'])])),
                ('content', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Les Accreditations de AHSM',
            },
        ),
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.FileField(default='', null=True, upload_to=Web.utils.upload_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif', 'jpeg', 'webp', 'svg', 'bmp'])])),
                ('name', models.CharField(max_length=150)),
                ('date', models.DateField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Les Collaborateurs de AHSM',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.FileField(default='', null=True, upload_to=Web.utils.upload_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif', 'jpeg', 'webp', 'svg', 'bmp'])])),
                ('lastname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=150)),
                ('category', models.CharField(choices=[('A', 'Direction'), ('B', 'Administrative'), ('C', 'Enseignants ')], max_length=2)),
                ('occupation', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Les Membres constituant AHSM',
            },
        ),
    ]
