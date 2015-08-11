# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_location_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='phone',
            field=models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
        ),
        migrations.AddField(
            model_name='location',
            name='website',
            field=models.URLField(max_length=500, null=True, blank=True),
        ),
    ]
