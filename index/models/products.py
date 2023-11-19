from django.db import models
from django.utils import timezone
from .suppliers import Supplier


class Product(models.Model):
    description = models.CharField(verbose_name='Descrição', max_length=99)
    sector = models.CharField(verbose_name='Setor',
                              choices=[], max_length=20, null=True, blank=True)
    unit = models.CharField(verbose_name='Unidade',
                            choices=[], max_length=5, null=True, blank=True)
    supplier = models.ForeignKey(
        Supplier, on_delete=models.DO_NOTHING, verbose_name='Fornecedor')
    manufacturer = models.CharField(verbose_name='Fabricante', max_length=99)
    cost = models.PositiveIntegerField(
        default=0, verbose_name='Preço de Custo')
    profit_margin = models.PositiveIntegerField(
        default=0, verbose_name='Margem de Lucro')
    stock = models.PositiveIntegerField(
        default=0, verbose_name='Quantidade em estoque')
    minimum_stock = models.PositiveIntegerField(
        default=0, verbose_name='Quantidade mínima')
    photo = models.ImageField(
        upload_to='media/products', null=True, blank=True)
    registration_date = models.DateTimeField(
        verbose_name='Data de cadastro', default=timezone.now)

    @property
    def sell_value(self):
        return self.cost + self.cost * (self.profit_margin / 100)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
