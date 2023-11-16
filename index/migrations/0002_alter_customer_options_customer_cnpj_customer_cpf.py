# Generated by Django 4.2.7 on 2023-11-16 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AddField(
            model_name='customer',
            name='cnpj',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='CNPJ'),
        ),
        migrations.AddField(
            model_name='customer',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='CPF'),
        ),
    ]
