# Generated by Django 3.1.4 on 2021-01-14 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_comment_revised'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='revised',
            field=models.BooleanField(default=False, verbose_name='revised'),
        ),
    ]
