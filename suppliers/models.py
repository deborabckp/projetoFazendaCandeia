from django.db import models


class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=20)
    cidade = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    anotacoes = models.TextField(blank=True, null=True)
    criadoEm = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.nome