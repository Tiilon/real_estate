# Generated by Django 3.2 on 2021-04-28 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0007_alter_house_acquisition_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='category',
            field=models.CharField(blank=True, choices=[('Hostel', 'Hostel'), ('Apartment', 'Apartment'), ('Flat', 'Flat'), ('Self-Contained', 'Self-Contained')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='listed_by',
            field=models.CharField(blank=True, choices=[('Agency', 'Agency'), ('Agent', 'Agent'), ('Owner', 'Owner')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='status',
            field=models.CharField(blank=True, choices=[(0, 'Unavailable'), (1, 'Available')], max_length=250, null=True),
        ),
    ]