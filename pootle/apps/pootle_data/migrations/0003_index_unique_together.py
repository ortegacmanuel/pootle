# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-19 09:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pootle_data', '0002_storechecksdata_tpchecksdata'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='storechecksdata',
            unique_together=set([('store', 'category', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='tpchecksdata',
            unique_together=set([('tp', 'category', 'name')]),
        ),
        migrations.AlterIndexTogether(
            name='storechecksdata',
            index_together=set([('name', 'category'), ('store', 'category', 'name')]),
        ),
        migrations.AlterIndexTogether(
            name='tpchecksdata',
            index_together=set([('name', 'category'), ('tp', 'category', 'name')]),
        ),
    ]