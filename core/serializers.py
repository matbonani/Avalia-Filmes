from rest_framework import serializers

from .models import Filme, Avaliacao


class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = (
            'id',
            'filme',
            'criacao',
            'atualizacao',
            'ativo'
        )


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'username',
            'email',
            'filme',
            'avaliacao',
            'criacao',
            'atualizacao',
            'ativo'

        )

