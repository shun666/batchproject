# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BatchWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('status', models.IntegerField(blank=True, null=True, verbose_name='Status')),
                ('category', models.IntegerField(blank=True, null=True, verbose_name='Category')),
                ('enabled', models.BooleanField(verbose_name='Enabled/Disabled')),
                ('value', models.DecimalField(blank=True, max_digits=10, null=True, verbose_name='Number', decimal_places=3)),
                ('memo', models.TextField(verbose_name='Memo')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
    ]
