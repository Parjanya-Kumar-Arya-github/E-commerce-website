# Generated by Django 3.1.7 on 2021-05-25 11:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dukan', '0008_auto_20210525_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saman',
            name='mfd',
            field=models.TimeField(default=datetime.datetime(2021, 5, 25, 11, 34, 9, 480779, tzinfo=utc)),
        ),
    ]
