# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 10:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0014_merge_20160920_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeegrade',
            name='employee',
            field=models.ForeignKey(help_text='Please select from existing employees.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique_for_date='g_start_date'),
        ),
        migrations.AlterField(
            model_name='employeegrade',
            name='grade',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, 'SES')], help_text='Please select a GS grade level.'),
        ),
    ]