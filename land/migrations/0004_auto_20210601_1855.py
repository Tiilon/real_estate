# Generated by Django 3.2 on 2021-06-01 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0003_auto_20210531_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='documents',
            field=models.FileField(blank=True, null=True, upload_to='land_docs/'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='duration',
            field=models.IntegerField(blank=True, choices=[(2, 'Two weeks'), (3, 'One Month'), (1, 'One week')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='acquisition_type',
            field=models.CharField(blank=True, choices=[('Sale', 'Sale'), ('Rent', 'Rent')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='land_type',
            field=models.CharField(blank=True, choices=[('Commercial', 'Commercial'), ('Agriculture', 'Agriculture'), ('Residential', 'Residential')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='lister',
            field=models.CharField(blank=True, choices=[('Agency', 'Agency'), ('Agent', 'Agent'), ('Owner', 'Owner')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='land',
            name='region',
            field=models.CharField(blank=True, choices=[('Northern', 'Northern'), ('Eastern', 'Eastern'), ('Ashanti', 'Ashanti'), ('Greater Accra', 'Greater Accra'), ('Western', 'Western')], max_length=250, null=True),
        ),
    ]