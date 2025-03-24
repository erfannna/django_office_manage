# Generated by Django 5.1.4 on 2025-01-01 19:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBuyOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('brand', models.CharField(max_length=50)),
                ('count', models.PositiveIntegerField(default=1)),
                ('order_type', models.CharField(choices=[('normal', 'عادی'), ('immediate', 'فوری')], max_length=20)),
                ('description', models.TextField(blank=True, max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_buy_orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductStockroomOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('brand', models.CharField(max_length=50)),
                ('count', models.PositiveIntegerField(default=1)),
                ('order_type', models.CharField(choices=[('normal', 'عادی'), ('immediate', 'فوری')], max_length=20)),
                ('description', models.TextField(blank=True, max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_stock_orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
