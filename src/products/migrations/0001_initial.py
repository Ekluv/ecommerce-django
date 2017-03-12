# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500, null=True, blank=True)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
