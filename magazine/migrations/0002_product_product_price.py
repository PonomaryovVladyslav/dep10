# Generated by Django 3.2.9 on 2021-11-28 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.PositiveIntegerField(default=10),
            preserve_default=False,
        ),
    ]
