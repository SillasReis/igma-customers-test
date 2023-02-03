from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from customer.models import Customer


class CustomersTestCase(APITestCase):
    fixtures = ['mock_customers']
    
    def setUp(self):
        self.list_url = reverse('Customers-list')
        self.valid_customers_data = [
            {
                'name': 'Ale Ale',
                'cpf': '293.893.210-34',
                'birth_date': '2015-01-27'
            },
            {
                'name': 'Ale Ale',
                'cpf': '09802757098',
                'birth_date': '2015-01-27'
            }
        ]

        self.invalid_customers_data = [
            {
                'name': 'Ale Ale2',
                'cpf': '293.893.210-34',
                'birth_date': '2015-01-27'
            },
            {
                'name': 'Ale',
                'cpf': '293.893.210-37',
                'birth_date': '2015-01-27'
            },
            {
                'name': 'Ale AAAle',
                'cpf': '293.893.210-34',
                'birth_date': datetime.now().date()
            }
        ]

    def test_list_customers(self):
        """Valida se os clientes estão sendo listados corretamente"""

        response = self.client.get(self.list_url)
        response_body = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_body['count'], 20)
        self.assertTrue(response_body['next'] is not None)
        self.assertTrue(response_body['previous'] is None)
        self.assertEqual(len(response_body['results']), 10)

    def test_create_customer(self):
        """Valida se um cliente é cadastrado com sucesso ao informar dados válidos"""

        for valid_customer_data in self.valid_customers_data:
            cleaned_cpf = valid_customer_data['cpf'].replace('-', '').replace('.', '')
            birth_date = datetime.strptime(valid_customer_data['birth_date'], '%Y-%m-%d').date()

            response = self.client.post(self.list_url, valid_customer_data)
            customer = Customer.objects.filter(cpf=cleaned_cpf).first()

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(customer.name, valid_customer_data['name'])
            self.assertEqual(customer.cpf, cleaned_cpf)
            self.assertEqual(customer.birth_date, birth_date)

    def test_create_customer_fails_with_invalid_data(self):
        """Valida se operação de cadastro falha quando dados do cliente são inválidos"""

        for invalid_customer_data in self.invalid_customers_data:
            response = self.client.post(self.list_url, invalid_customer_data)
            self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_create_customer_fails_when_cpf_exists_in_database(self):
        """Valida se a operação falha quando o cpf já existe na base"""

        customer_data = self.valid_customers_data[0]

        first_response = self.client.post(self.list_url, customer_data)
        second_response = self.client.post(self.list_url, customer_data)

        self.assertEqual(first_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(second_response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def test_delete_and_update_customer_unavailable(self):
        """Valida se os método DELETE, PUT e PATCH estão indisponíveis"""

        response_delete = self.client.delete('/customers/ac59a044-a332-11ed-9446-00155d2c54f7')
        response_put = self.client.put('/customers/ac59a044-a332-11ed-9446-00155d2c54f7')
        response_patch = self.client.patch('/customers/ac59a044-a332-11ed-9446-00155d2c54f7')

        self.assertEquals(response_delete.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEquals(response_put.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEquals(response_patch.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
