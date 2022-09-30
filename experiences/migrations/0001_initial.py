# Generated by Django 4.1.1 on 2022-09-29 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.CharField(default='한국', max_length=50)),
                ('city', models.CharField(default='서울', max_length=80)),
                ('name', models.CharField(max_length=250)),
                ('price', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=250)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Perk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=250)),
                ('explanation', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
