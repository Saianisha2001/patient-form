# Generated by Django 3.2.5 on 2021-07-28 19:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 29, 0, 41, 25, 861053)),
        ),
    ]
