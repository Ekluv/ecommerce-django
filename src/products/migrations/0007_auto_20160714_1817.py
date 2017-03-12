# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20160712_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='variation',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='variation',
            name='sale_price',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='products.Category', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='default',
            field=models.ForeignKey(related_name='default_category', blank=True, to='products.Category', null=True),
        ),
    ]
