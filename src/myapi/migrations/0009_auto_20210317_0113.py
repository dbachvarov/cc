# Generated by Django 3.0.2 on 2021-03-17 01:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0008_auto_20210317_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='expiration_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 19, 1, 13, 20, 700005)),
        ),
    ]
