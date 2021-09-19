"""
Aplicação front-end usando Streamlit para gerar a página
"""

import streamlit as st

# FIXME: Por algum motivo o streamlit não aceita importar as páginas
# via __init__.py ou importação relativa
# pylint: disable=import-error
import introducao
import questao_problema

# pylint: enable=import-error

# Sidebar
PAGES = {"Questão Problema": questao_problema.case, "Introdução": introducao.intro}

st.sidebar.title("Índice")
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page()
