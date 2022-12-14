# Generated by Django 4.1 on 2022-08-07 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0002_prod_category_alter_categ_name_alter_categ_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartid', models.CharField(max_length=50, unique=True)),
                ('dateadded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quant', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cartlist')),
                ('prodt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.prod')),
            ],
        ),
    ]
