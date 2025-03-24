# Generated by Django 5.1.4 on 2025-01-02 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_number',
            field=models.CharField(max_length=10, unique=True, verbose_name='کد ملی'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True, verbose_name='تلفن همراه'),
        ),
    ]
