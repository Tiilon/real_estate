# Generated by Django 3.2 on 2021-05-10 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0014_auto_20210510_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='number_of_page_visits',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='acquisition_type',
            field=models.CharField(blank=True, choices=[('Rent', 'Rent'), ('Sale', 'Sale')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='category',
            field=models.CharField(blank=True, choices=[('Self-Contained', 'Self-Contained'), ('Apartment', 'Apartment'), ('Flat', 'Flat'), ('Hostel', 'Hostel')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='listed_by',
            field=models.CharField(blank=True, choices=[('Owner', 'Owner'), ('Agent', 'Agent'), ('Agency', 'Agency')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='page_views',
            field=models.ManyToManyField(blank=True, related_name='house_views', to='estate.PageVisit'),
        ),
        migrations.AlterField(
            model_name='house',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Unavailable'), (1, 'Available')], null=True),
        ),
    ]
