# Generated by Django 3.0.8 on 2020-07-17 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200717_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_type',
            field=models.IntegerField(choices=[(1, 'student'), (2, 'professor'), (3, 'staff'), (4, 'undefined')], default=4),
        ),
    ]