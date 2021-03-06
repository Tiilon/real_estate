# Generated by Django 3.2 on 2021-05-10 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0015_auto_20210510_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='for_rent_amount',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='house',
            name='for_sale_price',
        ),
        migrations.AlterField(
            model_name='house',
            name='category',
            field=models.CharField(blank=True, choices=[('Apartment', 'Apartment'), ('Flat', 'Flat'), ('Hostel', 'Hostel'), ('Self-Contained', 'Self-Contained')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='listed_by',
            field=models.CharField(blank=True, choices=[('Agency', 'Agency'), ('Owner', 'Owner'), ('Agent', 'Agent')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'Available'), (0, 'Unavailable')], null=True),
        ),
    ]
