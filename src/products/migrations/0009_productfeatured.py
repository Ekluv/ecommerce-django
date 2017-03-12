# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20160714_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFeatured',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'products/featured/')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400, null=True, blank=True)),
                ('description_right', models.BooleanField(default=False)),
                ('show_price', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
    ]
