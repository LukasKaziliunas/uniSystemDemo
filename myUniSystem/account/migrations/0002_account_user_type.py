# Generated by Django 3.0.8 on 2020-07-17 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='user_type',
            field=models.IntegerField(choices=[(1, 'student'), (2, 'professor')], max_length=1, null=True),
        ),
    ]
