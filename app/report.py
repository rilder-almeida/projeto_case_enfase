import streamlit as st
import pandas as pd

# FIXME: Por algum motivo o streamlit não aceita importar as páginas
# via __init__.py ou importação relativa
# pylint: disable=import-error
from core import get_dataset

# pylint: enable=import-error


def report():
    "Função página Relatório - Pandas Profiling"
    st.title("Relatório - Pandas Profiling")
    st.markdown("Para algumas análises estatíticas foi utilizado o Pandas Profiling")
    st.markdown("Siga os passos:")
    st.code(
        """
git clone https://github.com/rilder-almeida/projeto_case_enfase && cd projeto_case_enfase
firefox Analysis.html

ou
chrome Analysis.html
    """
    )
