"""Módulo de funções dos widgets, gráficos, manupulação de datasets"""
import streamlit as st
import pandas as pd

# import plotly_express as px


@st.cache
def get_dataset(collumns: list = None):
    """Read logistica_dataset.csv

    Args:
        collumns (list, optional): selected collumns to return. Defaults to None.

    Returns:
        object pandas dataset: Returns the dataset with selected collumns
    """
    return pd.read_csv(
        "./data/logistica_dataset.csv", usecols=collumns, parse_dates=True
    )


# Função remanecente do template de projeto mantida para não gerar erro por ausência de
# algum teste no pytest durante o pre-commit
def sample_sum_func(num_a: int, num_b: int) -> int:
    """
    :rtype: object
    :param num_a: first number
    :param num_b: second number
    :return: sum of two numbers
    """
    sum_two_numbers: int = num_a + num_b
    return sum_two_numbers
