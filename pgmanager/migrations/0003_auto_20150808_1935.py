# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pgmanager', '0002_ec2instance_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ec2instance',
            name='startTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
