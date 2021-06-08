# Generated by Django 3.2 on 2021-05-31 16:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0002_auto_20210531_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='uuid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='advert',
            name='duration',
            field=models.IntegerField(blank=True, choices=[(1, 'One week'), (2, 'Two weeks'), (3, 'One Month')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='acquisition_type',
            field=models.CharField(blank=True, choices=[('Rent', 'Rent'), ('Sale', 'Sale')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='land_type',
            field=models.CharField(blank=True, choices=[('Residential', 'Residential'), ('Agriculture', 'Agriculture'), ('Commercial', 'Commercial')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='region',
            field=models.CharField(blank=True, choices=[('Greater Accra', 'Greater Accra'), ('Western', 'Western'), ('Eastern', 'Eastern'), ('Ashanti', 'Ashanti'), ('Northern', 'Northern')], max_length=250, null=True),
        ),
    ]
