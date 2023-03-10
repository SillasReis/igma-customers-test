from datetime import date


CPF_DIGITS_MULTIPLIERS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def validate_name(name: str) -> bool:
    return all(char.isalpha() or char.isspace() for char in name)


def validate_birth_date(birth_date: str) -> bool:
    return birth_date < date.today()


def validate_cpf(cpf: str) -> bool:
    if len(cpf) != 11:
        return False

    expected_cpf = cpf[0:9]

    for _ in range(2):
        sum = 0

        for digit, multiplier in zip(reversed(expected_cpf), CPF_DIGITS_MULTIPLIERS):
            sum += int(digit) * multiplier

        remainder = sum % 11

        expected_cpf += "0" if remainder < 2 else str(11 - remainder)

    return cpf == expected_cpf
