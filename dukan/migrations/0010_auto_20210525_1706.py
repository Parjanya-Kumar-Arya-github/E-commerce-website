# Generated by Django 3.1.7 on 2021-05-25 11:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dukan', '0009_auto_20210525_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='id',
            new_name='cont_id',
        ),
        migrations.AlterField(
            model_name='saman',
            name='mfd',
            field=models.TimeField(default=datetime.datetime(2021, 5, 25, 11, 36, 2, 260895, tzinfo=utc)),
        ),
    ]