# Generated by Django 3.0.2 on 2021-03-12 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20210311_2335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]