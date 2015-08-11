# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='alcohol',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='location',
            name='bathrooms',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='location',
            name='coffee_quality',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'BAD', b'Bad'), (b'OKAY', b'Okay'), (b'GOOD', b'Good'), (b'GREAT', b'Great')]),
        ),
        migrations.AddField(
            model_name='location',
            name='food',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='location',
            name='outdoor_seating',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='location',
            name='outlets',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'NONE', b'None'), (b'SOME', b'Some'), (b'PLENTY', b'Plenty')]),
        ),
        migrations.AddField(
            model_name='location',
            name='seating_cap',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'LIMITED', b'Limited'), (b'AVERAGE', b'Average'), (b'AMPLE', b'Ample')]),
        ),
        migrations.AddField(
            model_name='location',
            name='wifi',
            field=models.NullBooleanField(),
        ),
    ]
