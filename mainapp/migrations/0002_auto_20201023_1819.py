# Generated by Django 3.1.2 on 2020-10-23 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 23, 18, 19, 39, 381122)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 23, 18, 19, 39, 381692)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 23, 18, 19, 39, 382908)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 23, 18, 19, 39, 382928)),
        ),
        migrations.AlterField(
            model_name='responces',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 23, 18, 19, 39, 382209)),
        ),
    ]
