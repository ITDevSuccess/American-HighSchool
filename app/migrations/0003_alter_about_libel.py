# Generated by Django 4.2.2 on 2023-06-17 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_about_content_alter_about_libel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='libel',
            field=models.CharField(max_length=250),
        ),
    ]
