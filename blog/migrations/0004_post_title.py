# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170719_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='text set', max_length=100),
            preserve_default=False,
        ),
    ]