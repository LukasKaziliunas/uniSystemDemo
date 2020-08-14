# Generated by Django 3.0.8 on 2020-07-26 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_groupsubjects_classroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='studygroup',
            name='semester',
            field=models.CharField(choices=[('1', '1st'), ('2', '2nd'), ('3', '3rd'), ('4', '4th'), ('5', '5th'), ('6', '6th'), ('7', '7th'), ('8', '8th')], default='0', max_length=1),
        ),
    ]
