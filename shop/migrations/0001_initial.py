# Generated by Django 4.1 on 2022-08-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='prod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('img', models.ImageField(upload_to='images')),
                ('desc', models.TextField()),
                ('stock', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]