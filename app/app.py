"""
Aplicação front-end usando Streamlit para gerar a página
"""

import streamlit as st

# FIXME: Por algum motivo o streamlit não aceita importar as páginas
# via __init__.py ou importação relativa
# pylint: disable=import-error
import introducao
import questao_problema
import analise_prazos_x_atrasos

# pylint: enable=import-error

# Sidebar
PAGES = {
    "Questão Problema": questao_problema.case,
    "Introdução": introducao.intro,
    "Análise Prazos e Atrasos": analise_prazos_x_atrasos.prazos_atrasos,
}

st.sidebar.title("Índice")
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page()
