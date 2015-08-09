# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pgmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ec2instance',
            name='ip',
            field=models.CharField(default='0.0.0.0', max_length=50),
        ),
    ]
