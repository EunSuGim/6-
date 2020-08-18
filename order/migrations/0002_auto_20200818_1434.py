# Generated by Django 3.0.8 on 2020-08-18 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desserts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('cd', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('gram', models.IntegerField()),
                ('allergy', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'Desserts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('cd', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'Goods',
                'managed': False,
            },
        ),
        migrations.AlterModelTable(
            name='coffee',
            table='Coffee',
        ),
    ]