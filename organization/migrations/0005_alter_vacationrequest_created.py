# Generated by Django 5.1.4 on 2025-01-02 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_vacationrequest_created_alter_vacationrequest_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacationrequest',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
