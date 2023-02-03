from django.test import TestCase

from customer.models import Customer
from customer.serializers import CustomerSerializer


class CustomerSerializerTestCase(TestCase):
    def setUp(self):
        self.customer = Customer(
            name='Tchurusmango Tchurusmago',
            cpf='57316059044',
            birth_date='2015-07-28',
        )

        self.serializer = CustomerSerializer(instance=self.customer)

    def test_serialized_fields(self):
        """Valida se os campos corretos estão sendo serializados"""

        fields = set(self.serializer.data.keys())
        self.assertEqual(fields, {'id', 'name', 'cpf', 'birth_date'})

    def test_serialized_values(self):
        """Valida se os campos estão sendo adequadamente passados pelo serializer"""

        data = self.serializer.data

        self.assertEqual(data['cpf'], self.customer.cpf)
        self.assertEqual(data['name'], self.customer.name)
        self.assertEqual(data['birth_date'], self.customer.birth_date)
