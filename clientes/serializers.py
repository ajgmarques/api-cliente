from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import (
    cpf_valido, nome_valido, rg_valido, celular_valido)


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError(
                {"cpf": 'Cpf inválido'})

        if not nome_valido(data['nome']):
            raise serializers.ValidationError(
                {"nome": 'O campo não pode ter números'})

        if not rg_valido(data['rg']):
            raise serializers.ValidationError(
                {"rg": 'O rg deve ter 9 digitos'})

        if not celular_valido(data['celular']):
            raise serializers.ValidationError(
                {"celular": 'Modelo do celular: 85 12345-6789, respeitando o espaço e traço'})

        return data
