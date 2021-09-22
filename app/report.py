import streamlit as st
import pandas as pd

# FIXME: Por algum motivo o streamlit não aceita importar as páginas
# via __init__.py ou importação relativa
# pylint: disable=import-error
from core import get_dataset

# pylint: enable=import-error


def report():
    "Função página Relatório - Pandas Profiling"
    st.title("Relatório -Pandas Profiling")
    st.markdown("Para algumas análises estatíticas foi utilisizado o Pandas Profiling")
    st.markdown("Baixe [aqui]('.../projeto_case_enfase/Analysis.html')")
