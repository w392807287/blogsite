# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import DjangoUeditor.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160911_0953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pub_date'], 'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u6587\u7ae0'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='date_time',
        ),
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 11, 2, 55, 56, 663301, tzinfo=utc), verbose_name='\u53d1\u5e03\u65e5\u671f', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(max_length=50, verbose_name='\u535a\u5ba2\u6807\u7b7e', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u6587\u7ae0\u6b63\u6587', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name='\u535a\u5ba2\u6807\u9898'),
        ),
    ]
