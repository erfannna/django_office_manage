# Generated by Django 5.1.4 on 2025-01-03 10:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_problemreport_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemreport',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
