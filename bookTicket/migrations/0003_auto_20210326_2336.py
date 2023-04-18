# Generated by Django 3.1.5 on 2021-03-26 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookTicket', '0002_remove_busdetails_journeydate'),
    ]

    operations = [
        migrations.CreateModel(
            name='ticketDetail',
            fields=[
                ('ticketID', models.AutoField(primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=50)),
                ('busID', models.IntegerField()),
                ('journeyDate', models.DateField()),
                ('totalFare', models.IntegerField(default=0)),
                ('seatNo', models.CharField(max_length=2)),
                ('passName', models.CharField(max_length=50)),
                ('passAge', models.IntegerField()),
                ('PassGender', models.CharField(max_length=7)),
            ],
        ),
        migrations.AlterField(
            model_name='busdetails',
            name='bookedSeat',
            field=models.CharField(max_length=100),
        ),
    ]