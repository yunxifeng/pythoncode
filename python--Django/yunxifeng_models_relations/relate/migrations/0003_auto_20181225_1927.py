# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relate', '0002_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_name',
            field=models.CharField(max_length=20),
        ),
    ]
