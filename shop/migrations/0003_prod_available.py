# Generated by Django 4.1 on 2022-08-08 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_prod_category_alter_categ_name_alter_categ_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prod',
            name='available',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
