# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-01 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GPKGManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geopackage',
            name='File',
            field=models.FileField(null=True, upload_to=b'geopackages/'),
        ),
    ]
