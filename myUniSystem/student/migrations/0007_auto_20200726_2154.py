# Generated by Django 3.0.8 on 2020-07-26 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_studygroup_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studygroup',
            name='semester',
            field=models.CharField(choices=[('1', '1st'), ('2', '2nd'), ('3', '3rd'), ('4', '4th'), ('5', '5th'), ('6', '6th'), ('7', '7th'), ('8', '8th')], max_length=1),
        ),
    ]
