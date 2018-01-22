# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-29 16:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0023_userdata_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.Organization'),
        ),
    ]