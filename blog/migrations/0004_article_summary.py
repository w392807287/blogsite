# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160911_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.TextField(default='\u8c8c\u4f3c\u6ca1\u6709\u5199\u7b80\u4ecb', verbose_name='\u6587\u7ae0\u7b80\u4ecb', blank=True),
        ),
    ]
