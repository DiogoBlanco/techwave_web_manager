# Generated by Django 4.2.7 on 2023-11-17 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='base_static/img/products'),
        ),
    ]
