# Generated by Django 3.2 on 2021-05-31 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='rent_duration',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='land',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'Available'), (0, 'Unavailable')], null=True),
        ),
        migrations.AlterField(
            model_name='advert',
            name='duration',
            field=models.IntegerField(blank=True, choices=[(2, 'Two weeks'), (1, 'One week'), (3, 'One Month')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='land_type',
            field=models.CharField(blank=True, choices=[('Commercial', 'Commercial'), ('Agriculture', 'Agriculture'), ('Residential', 'Residential')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='lister',
            field=models.CharField(blank=True, choices=[('Agent', 'Agent'), ('Owner', 'Owner'), ('Agency', 'Agency')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='region',
            field=models.CharField(blank=True, choices=[('Greater Accra', 'Greater Accra'), ('Eastern', 'Eastern'), ('Western', 'Western'), ('Northern', 'Northern'), ('Ashanti', 'Ashanti')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='unit',
            field=models.CharField(blank=True, choices=[('Acres', 'Acres'), ('Sqft', 'Sqft'), ('Plot', 'Plot')], max_length=250, null=True),
        ),
    ]
