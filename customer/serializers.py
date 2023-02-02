from rest_framework import serializers

from customer import validators
from customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def validate(self, data: dict):
        if not validators.validate_cpf(data.get('cpf')):
            raise serializers.ValidationError({'cpf': 'CPF inválido.'})

        if not validators.validate_name(data.get('name')):
            raise serializers.ValidationError(
                {'name': 'Nome inválido. O nome deve conter apenas letras, espaços e, no máximo, 100 caracteres.'},
            )

        if not validators.validate_birth_date(data.get('birth_date')):
            raise serializers.ValidationError({'birth_date': 'A data de nascimento deve estar no passado.'})

        return data

    def to_internal_value(self, data):
        _mutable = data._mutable
        data._mutable = True

        data['cpf'] = data['cpf'].replace('-', '').replace('.', '')

        data._mutable = _mutable

        return super(CustomerSerializer, self).to_internal_value(data)
