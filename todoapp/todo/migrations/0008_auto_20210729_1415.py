# Generated by Django 3.1.7 on 2021-07-29 08:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_alter_todo_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 29, 14, 15, 16, 504475)),
        ),
    ]
