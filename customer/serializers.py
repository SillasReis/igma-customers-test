from rest_framework import serializers

from customer import validators
from customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def validate(self, fields: dict):
        if not validators.validate_cpf(fields.get('cpf', '')):
            # TODO: ACCEPT MASKED CPF
            raise serializers.ValidationError({'cpf': 'CPF inválido.'}, 422)

        if not validators.validate_name(fields.get('name', '')):
            raise serializers.ValidationError(
                {'name': 'Nome inválido. O nome deve conter apenas letras, espaços e, no máximo, 100 caracteres.'},
                422
            )

        return fields
