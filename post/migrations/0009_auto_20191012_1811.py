# Generated by Django 2.1 on 2019-10-12 22:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20191012_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.TimeField(default=datetime.datetime(2019, 10, 12, 22, 11, 19, 719504, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.TimeField(default=datetime.datetime(2019, 10, 12, 22, 11, 19, 717505, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
