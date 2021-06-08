# Generated by Django 3.2 on 2021-05-04 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0010_auto_20210504_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='category',
            field=models.CharField(blank=True, choices=[('Apartment', 'Apartment'), ('Hostel', 'Hostel'), ('Self-Contained', 'Self-Contained'), ('Flat', 'Flat')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='listed_by',
            field=models.CharField(blank=True, choices=[('Owner', 'Owner'), ('Agent', 'Agent'), ('Agency', 'Agency')], max_length=250, null=True),
        ),
    ]