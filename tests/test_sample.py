# FIXME Testes não implementados devido ao tempo reduzido para execução do projeto

from .context import app
from app import sample_sum_func
from pytest import mark


@mark.parametrize("num_a,num_b,expected", [(1, 2, 3), (-3, 4, 1), (-1.7, 0.6, -1.1)])
def test_sample_sum_func(num_a, num_b, expected):
    """testing sum_func"""
    result = sample_sum_func(num_a, num_b)
    assert result == expected
