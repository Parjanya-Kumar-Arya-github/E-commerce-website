# Generated by Django 3.1.7 on 2021-05-24 12:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dukan', '0002_saman_mfd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saman',
            name='mfd',
            field=models.DateField(default=datetime.datetime(2021, 5, 24, 12, 24, 41, 587629, tzinfo=utc)),
        ),
    ]