# Generated by Django 3.0.8 on 2020-07-29 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0006_auto_20200729_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='timetables',
            field=models.ManyToManyField(blank=True, related_name='weeks', to='timetable.Timetable'),
        ),
    ]