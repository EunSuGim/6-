# Generated by Django 3.0.8 on 2020-08-19 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20200819_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='cd',
            field=models.IntegerField(null=True),
        ),
    ]
