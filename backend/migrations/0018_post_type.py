# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-02 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_auto_20170506_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.IntegerField(choices=[(1, 'Post'), (2, 'Tip'), (3, 'Diet')], default=1),
        ),
    ]