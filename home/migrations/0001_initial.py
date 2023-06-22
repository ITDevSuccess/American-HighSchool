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
            name='Possibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Les Possibilités',
            },
        ),
        migrations.CreateModel(
            name='PresentationImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.FileField(default='', null=True, upload_to=Web.utils.upload_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif', 'jpeg', 'webp', 'svg', 'bmp'])])),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Les Présentations Photo AHSM',
            },
        ),
        migrations.CreateModel(
            name='PresentationVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('video', models.FileField(default='', upload_to=Web.utils.upload_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov'])])),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Les Présentations Vidéo AHSM',
            },
        ),
    ]