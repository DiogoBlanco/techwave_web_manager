# Generated by Django 4.2.7 on 2023-11-17 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_customer_registration_date_product_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/products'),
        ),
    ]
