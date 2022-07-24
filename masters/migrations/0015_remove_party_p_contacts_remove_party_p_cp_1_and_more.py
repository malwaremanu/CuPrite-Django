# Generated by Django 4.0.6 on 2022-07-24 02:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0014_party_p_contacts_alter_party_p_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='p_contacts',
        ),
        migrations.RemoveField(
            model_name='party',
            name='p_cp_1',
        ),
        migrations.RemoveField(
            model_name='party',
            name='p_cp_2',
        ),
        migrations.RemoveField(
            model_name='party',
            name='p_id',
        ),
        migrations.AddField(
            model_name='party',
            name='p_contacts_email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='party',
            name='p_contacts_fax',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='party',
            name='p_contacts_phone',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='party',
            name='p_contacts_website',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='party',
            name='p_cp_1_email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='party',
            name='p_cp_1_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='party',
            name='p_cp_1_phone',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='party',
            name='p_cp_2_email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='party',
            name='p_cp_2_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='party',
            name='p_cp_2_phone',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='party',
            name='p_id_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='party',
            name='p_id_nif',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='party',
            name='p_id_rccm',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='party',
            name='p_id_tva',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='party',
            name='p_author',
            field=models.CharField(default='System', max_length=100),
        ),
        migrations.AlterField(
            model_name='party',
            name='p_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 24, 2, 49, 39, 404557)),
        ),
    ]