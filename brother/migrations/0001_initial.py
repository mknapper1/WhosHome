# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 01:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac', models.CharField(max_length=17)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('type', models.CharField(blank=True, max_length=25)),
                ('home', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_date', models.DateTimeField(verbose_name='date changed')),
                ('home', models.BooleanField(default=False)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brother.Device')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('permissions', models.CharField(blank=True, default='user', max_length=10)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('pet', models.BooleanField(default=False)),
                ('home', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brother.User'),
        ),
    ]
