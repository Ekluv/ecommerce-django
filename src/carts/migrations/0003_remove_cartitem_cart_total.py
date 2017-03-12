# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cartitem_cart_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart_total',
        ),
    ]
