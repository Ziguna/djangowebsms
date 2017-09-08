# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 11:36
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('number', models.CharField(blank=True, max_length=200, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')])),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.CharField(blank=True, max_length=200, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')]),
        ),
        migrations.DeleteModel(
            name='Receiver',
        ),
        migrations.DeleteModel(
            name='Sender',
        ),
    ]