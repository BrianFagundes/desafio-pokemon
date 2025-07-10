# core/models.py

from django.db import models

class Tipo(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome")

    def __str__(self):
        return self.nome

class Pokemon(models.Model):
    codigo = models.IntegerField(primary_key=True, verbose_name="Código")
    nome = models.CharField(max_length=100, verbose_name="Nome")
    tipo_primario = models.ForeignKey(Tipo, on_delete=models.PROTECT, related_name='pokemons_primarios', verbose_name="Tipo Primário")
    tipo_secundario = models.ForeignKey(
        Tipo,
        on_delete=models.PROTECT,
        related_name='pokemons_secundarios',
        null=True,
        blank=True,
        verbose_name="Tipo Secundário"
    )

    class Meta:
        verbose_name = "Pokemon"
        verbose_name_plural = "Pokemons"
        ordering = ['codigo']

    def __str__(self):
        return f"#{self.codigo:03} - {self.nome}"