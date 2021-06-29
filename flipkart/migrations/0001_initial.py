# Generated by Django 3.1.4 on 2021-01-28 04:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlipKart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('desired_price', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('date_time', models.DateTimeField(default=datetime.datetime(2021, 1, 28, 9, 58, 2, 348823))),
            ],
        ),
    ]
