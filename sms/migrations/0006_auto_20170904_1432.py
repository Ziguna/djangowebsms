# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0005_remove_file_fill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
