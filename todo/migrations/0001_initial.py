# Generated by Django 4.1.5 on 2023-01-12 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
    ]
