# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('preview', tinymce.models.HTMLField()),
                ('content', tinymce.models.HTMLField()),
                ('read', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(verbose_name='Description', max_length=150)),
            ],
        ),
    ]
