# Generated by Django 3.1.7 on 2021-08-02 09:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0014_auto_20210802_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
