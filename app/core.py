"""Sample function"""

# Função remanecente do template do projeto original para não gerar erro no
# pytest de ausẽncia de testes durante o pre-commit


def sample_sum_func(num_a: int, num_b: int) -> int:
    """
    :rtype: object
    :param num_a: first number
    :param num_b: second number
    :return: sum of two numbers
    """
    sum_two_numbers: int = num_a + num_b
    return sum_two_numbers
