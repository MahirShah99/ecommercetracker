# Generated by Django 3.1.4 on 2021-02-06 11:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipkart', '0004_auto_20210206_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flipkart',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 6, 16, 49, 4, 560376)),
        ),
    ]
