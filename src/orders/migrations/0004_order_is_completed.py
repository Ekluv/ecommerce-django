# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_completed',
            field=models.BooleanField(default=True),
        ),
    ]
