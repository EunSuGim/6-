# Generated by Django 3.0.8 on 2020-08-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_num',
            field=models.CharField(default=0, max_length=13, verbose_name='전화번호'),
        ),
    ]
