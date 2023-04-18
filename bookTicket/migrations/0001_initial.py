# Generated by Django 3.1.5 on 2021-03-22 17:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='busDetails',
            fields=[
                ('busID', models.AutoField(primary_key=True, serialize=False)),
                ('arrival', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('rent', models.IntegerField()),
                ('distance', models.IntegerField()),
                ('journeyDate', models.DateField(default=datetime.date.today)),
                ('bookedSeat', models.CharField(max_length=50)),
                ('time1', models.TimeField()),
                ('time2', models.TimeField()),
            ],
        ),
    ]