from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=99, verbose_name='Nome')
    address = models.CharField(max_length=99, verbose_name='Endereço')
    number = models.CharField(max_length=99, verbose_name='Número')
    district = models.CharField(max_length=99, verbose_name='Bairro')
    city = models.CharField(max_length=99, verbose_name='Cidade')
    state = models.CharField(choices=[
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
        ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'),
        ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'),
        ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'), ('RN',
                                   'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC',
                                                'Santa Catarina'), ('SP', 'São Paulo'),
        ('SE', 'Sergipe'), ('TO', 'Tocantins')
    ], verbose_name='Estado', max_length=19)
    zip_code = models.CharField(max_length=9, verbose_name='CEP')
    phone = models.CharField(max_length=15, verbose_name='Telefone')
    email = models.EmailField(verbose_name='E-mail')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'