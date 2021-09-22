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
