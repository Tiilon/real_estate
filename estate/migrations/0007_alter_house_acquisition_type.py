# Generated by Django 3.2 on 2021-04-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0006_auto_20210428_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='acquisition_type',
            field=models.CharField(blank=True, choices=[('Sale', 'Sale'), ('Rent', 'Rent')], max_length=100, null=True),
        ),
    ]
