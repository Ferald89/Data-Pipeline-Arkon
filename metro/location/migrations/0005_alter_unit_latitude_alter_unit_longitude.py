# Generated by Django 4.0.4 on 2022-05-16 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0004_rename_township_district_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]
