# Generated by Django 3.0.8 on 2020-08-01 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20200726_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupsubjects',
            name='classroom',
        ),
    ]
