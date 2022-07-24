# Generated by Django 4.0.6 on 2022-07-23 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0011_rename_p_address_party_p_address_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='p_address_1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='party',
            name='p_address_2',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='party',
            name='p_author',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='party',
            name='p_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 23, 15, 12, 38, 668730)),
        ),
    ]
