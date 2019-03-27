# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('room_id', models.IntegerField()),
                ('room_location', models.CharField(max_length=20)),
                ('room_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('stu_name', models.CharField(max_length=20)),
                ('stu_age', models.IntegerField()),
                ('room', models.ForeignKey(to='myAdmin.ClassRoom')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tea_name', models.CharField(max_length=5)),
                ('course', models.CharField(max_length=20)),
                ('room', models.OneToOneField(to='myAdmin.ClassRoom')),
            ],
        ),
    ]
