# Generated by Django 3.1.13 on 2022-07-18 10:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('masters', '0005_auto_20220718_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='PO',
            fields=[
                ('p_uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('p_no', models.CharField(max_length=200, unique=True)),
                ('p_date', models.DateTimeField()),
                ('p_from_company', models.TextField()),
                ('p_is_active', models.BooleanField()),
                ('p_tva_percentage', models.IntegerField()),
                ('po_supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masters.party')),
            ],
        ),
    ]