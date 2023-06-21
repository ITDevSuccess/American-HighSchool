# Generated by Django 4.2.2 on 2023-06-21 04:17

import Web.utils
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.FileField(default='', null=True, upload_to=Web.utils.upload_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'gif', 'jpeg', 'webp', 'svg', 'bmp'])])),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('promotion', models.FloatField(blank=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('price_promo', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('registration', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('birth', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31'), (32, '32'), (33, '33'), (34, '34'), (35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'), (40, '40'), (41, '41'), (42, '42'), (43, '43'), (44, '44'), (45, '45'), (46, '46'), (47, '47'), (48, '48'), (49, '49'), (50, '50'), (51, '51'), (52, '52'), (53, '53'), (54, '54'), (55, '55'), (56, '56'), (57, '57'), (58, '58'), (59, '59'), (60, '60'), (61, '61'), (62, '62'), (63, '63'), (64, '64'), (65, '65'), (66, '66'), (67, '67'), (68, '68'), (69, '69'), (70, '70'), (71, '71')], validators=[django.core.validators.MaxValueValidator(70), django.core.validators.MinValueValidator(2)])),
            ],
            options={
                'verbose_name_plural': 'Les Prix de formation ASHM',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('status', models.BooleanField(default=True)),
                ('prices', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='price.price')),
            ],
            options={
                'verbose_name_plural': "Les Niveaux d'Etude existant a l'AHSM",
            },
        ),
    ]
