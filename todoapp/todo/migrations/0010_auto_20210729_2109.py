# Generated by Django 3.1.7 on 2021-07-29 15:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_auto_20210729_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 29, 21, 9, 24, 230811)),
        ),
    ]
