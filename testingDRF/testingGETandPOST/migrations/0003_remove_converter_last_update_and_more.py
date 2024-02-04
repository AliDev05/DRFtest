# Generated by Django 4.2.9 on 2024-02-04 13:19

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testingGETandPOST', '0002_remove_converter_ac_freq_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='converter',
            name='last_update',
        ),
        migrations.AddField(
            model_name='converter',
            name='last_update_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='converter',
            name='last_update_time',
            field=models.TimeField(default=datetime.datetime(2024, 2, 4, 13, 19, 33, 369737, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]