from django.db import models
from suppliers.models import Fornecedor


class MilkPurchase(models.Model):
    fornecedor = models.ForeignKey(
        Fornecedor,
        on_delete=models.CASCADE,
        related_name='compras_leite'
    )

    data = models.DateField()
    litros = models.DecimalField(max_digits=10, decimal_places=2)
    precoPorLitro = models.DecimalField(max_digits=10, decimal_places=2)
    totalPreco = models.DecimalField(max_digits=10, decimal_places=2)
    anotacoes = models.TextField(blank=True, null=True)
    criadoEm = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Compra de Leite'
        verbose_name_plural = 'Compras de Leite'

    def save(self, *args, **kwargs):
        self.totalPreco = self.litros * self.precoPorLitro
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.fornecedor.nome} - {self.data}'