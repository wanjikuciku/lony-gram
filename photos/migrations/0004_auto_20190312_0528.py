# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-12 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20190312_0514'),
    ]

    operations = [
        migrations.CreateModel(
            name='idss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='likemodel',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='likemodel',
            name='user',
        ),
        migrations.DeleteModel(
            name='LikeModel',
        ),
    ]