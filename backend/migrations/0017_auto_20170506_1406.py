# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-06 14:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_auto_20170506_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tip',
            old_name='photos',
            new_name='images',
        ),
    ]