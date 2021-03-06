# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-20 07:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle', models.CharField(max_length=45)),
                ('pu_location', models.CharField(max_length=45)),
                ('pu_date', models.DateField(null=True)),
                ('pu_time', models.TimeField(null=True)),
                ('do_location', models.CharField(max_length=45)),
                ('do_date', models.DateField(null=True)),
                ('do_time', models.TimeField(null=True)),
                ('rate', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('made_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='made_by', to='login.User')),
            ],
        ),
    ]
