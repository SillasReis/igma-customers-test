import os
import sys
from random import randint

import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from customer.models import Customer  #noqa
from customer.validators import CPF_DIGITS_MULTIPLIERS  #noqa


def generate_cpf() -> str:
    cpf = [randint(0, 9) for _ in range(9)]

    for _ in range(2):
        sum = 0

        for digit, multiplier in zip(reversed(cpf), CPF_DIGITS_MULTIPLIERS):
            sum += digit * multiplier

        remainder = sum % 11

        cpf.append(0 if remainder < 2 else 11 - remainder)

    return ''.join(map(str, cpf))


def mock_customers(amount: int):
    for _ in range(amount):
        fake = Faker()

        name = fake.name()
        cpf = generate_cpf()
        birth_date = fake.date_between(start_date='-90y', end_date='-15y')

        Customer(name=name, cpf=cpf, birth_date=birth_date).save()


if __name__ == '__main__':
    try:
        amount = int(sys.argv[1])
    except (IndexError, ValueError):
        print("usage: python mock_customers.py <amount: int>")
        exit(1)

    mock_customers(amount)
