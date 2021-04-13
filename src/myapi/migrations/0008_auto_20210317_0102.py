# Generated by Django 3.0.2 on 2021-03-17 01:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0007_auto_20210316_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='expiration_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 19, 1, 2, 7, 677533)),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Live', 'Live'), ('Expired', 'Expired')], default='Live', max_length=10),
        ),
    ]