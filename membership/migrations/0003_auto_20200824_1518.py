# Generated by Django 3.0.3 on 2020-08-24 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_histories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='histories',
            name='order_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]