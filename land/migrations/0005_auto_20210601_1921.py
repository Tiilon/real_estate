# Generated by Django 3.2 on 2021-06-01 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0004_auto_20210601_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='lister_profile',
            field=models.FileField(blank=True, null=True, upload_to='lister_profile/'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='duration',
            field=models.IntegerField(blank=True, choices=[(3, 'One Month'), (1, 'One week'), (2, 'Two weeks')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='acquisition_type',
            field=models.CharField(blank=True, choices=[('Rent', 'Rent'), ('Sale', 'Sale')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='lister',
            field=models.CharField(blank=True, choices=[('Owner', 'Owner'), ('Agency', 'Agency'), ('Agent', 'Agent')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='region',
            field=models.CharField(blank=True, choices=[('Northern', 'Northern'), ('Ashanti', 'Ashanti'), ('Greater Accra', 'Greater Accra'), ('Eastern', 'Eastern'), ('Western', 'Western')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='unit',
            field=models.CharField(blank=True, choices=[('Acres', 'Acres'), ('Plot', 'Plot'), ('Sqft', 'Sqft')], max_length=250, null=True),
        ),
    ]