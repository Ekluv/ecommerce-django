# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100, choices=[(b'billing', b'Billing'), (b'shipping', b'Shipping')])),
                ('address', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.PositiveIntegerField()),
                ('user', models.ForeignKey(to='orders.UserCheckout')),
            ],
        ),
    ]
