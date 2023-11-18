from django.db import models
from django.utils import timezone


class Supplier(models.Model):
    company = models.CharField(verbose_name='Empresa', max_length=99)
    contact = models.CharField(
        verbose_name='Contato', max_length=99, null=True, blank=True)
    address = models.CharField(verbose_name='Endereço', max_length=99)
    number = models.CharField(max_length=99, verbose_name='Número')
    district = models.CharField(verbose_name='Bairro', max_length=99)
    city = models.CharField(verbose_name='Cidade', max_length=99)
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
    cnpj = models.CharField(verbose_name='CNPJ',
                            max_length=18, blank=True, null=True)
    registration_date = models.DateTimeField(
        verbose_name='Data de cadastro', default=timezone.now)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.company
