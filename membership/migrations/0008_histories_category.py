# Generated by Django 3.0.3 on 2020-08-24 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0007_histories_cd'),
    ]

    operations = [
        migrations.AddField(
            model_name='histories',
            name='category',
            field=models.CharField(max_length=20, null=True, verbose_name='카테고리'),
        ),
    ]
