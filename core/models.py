from django.db import models

from django.core.exceptions import ValidationError


def valida_nota(value):
    if value > 5 or value < 0:
        raise ValidationError('Valor incorreto! Valor prescisa ser entre 0 e 5')
    else:
        return value


class Base(models.Model):
    criacao = models.DateField('Criação', auto_now_add=True)
    atualizacao = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Filme(Base):
    filme = models.CharField('Nome do Filme', unique=True, max_length=150)

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'

    def __str__(self):
        return self.filme


class Avaliacao(Base):
    username = models.CharField('Username', max_length=105)
    email = models.EmailField('Email')
    filme = models.ForeignKey(Filme, related_name='avaliacoes', on_delete=models.CASCADE)
    avaliacao = models.DecimalField(validators=[valida_nota], decimal_places=1, max_digits=2)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['username', 'filme']

    def __str__(self):
        return f'Avaliação de {self.username}'
