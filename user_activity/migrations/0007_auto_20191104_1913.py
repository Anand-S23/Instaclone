# Generated by Django 2.1 on 2019-11-04 19:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_activity', '0006_auto_20191102_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act',
            name='act_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 4, 19, 13, 40, 931944)),
        ),
    ]
