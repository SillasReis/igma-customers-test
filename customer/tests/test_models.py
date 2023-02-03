from uuid import UUID

from django.test import TestCase

from customer.models import Customer


class CustomersTestCase(TestCase):
    def setUp(self):
        self.customer = Customer(
            name='Tchurusmango Tchurusmago',
            cpf='57316059044',
            birth_date='2015-07-28',
        )

    def test_validate_default_uuid_generator(self):
        """Valida se o id gerado automaticamente é um UUID válido"""

        self.assertTrue(isinstance(self.customer.id, UUID))
