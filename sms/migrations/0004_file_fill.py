# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='fill',
            field=models.CharField(blank=True, max_length=True),
        ),
    ]