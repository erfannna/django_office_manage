# Generated by Django 5.1.4 on 2025-03-14 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0010_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacationrequest',
            name='status',
            field=models.CharField(choices=[('بررسی نشده', 'بررسی نشده'), ('تایید جانشین', 'تایید جانشین'), ('رد جانشین', 'رد جانشین'), ('موافقت شده', 'موافقت شده'), ('رد شده', 'رد شده')], default='بررسی نشده', max_length=20, verbose_name='وضعیت مرخصی'),
        ),
    ]
