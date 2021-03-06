# Generated by Django 3.2 on 2021-04-30 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0008_auto_20210428_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='acquisition_type',
            field=models.CharField(blank=True, choices=[('Rent', 'Rent'), ('Sale', 'Sale')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='category',
            field=models.CharField(blank=True, choices=[('Apartment', 'Apartment'), ('Self-Contained', 'Self-Contained'), ('Hostel', 'Hostel'), ('Flat', 'Flat')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='listed_by',
            field=models.CharField(blank=True, choices=[('Owner', 'Owner'), ('Agency', 'Agency'), ('Agent', 'Agent')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='status',
            field=models.CharField(blank=True, choices=[(1, 'Available'), (0, 'Unavailable')], max_length=250, null=True),
        ),
    ]
