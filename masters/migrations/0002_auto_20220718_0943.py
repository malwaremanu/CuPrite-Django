# Generated by Django 3.1.13 on 2022-07-18 09:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='p_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 18, 9, 43, 8, 181809)),
        ),
    ]
