# Generated by Django 3.1.4 on 2020-12-17 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20201214_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_verified',
            field=models.BooleanField(default=True, verbose_name='verified'),
        ),
    ]