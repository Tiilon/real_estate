# Generated by Django 3.2 on 2021-04-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210428_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rest_password',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
