"""
Módulo da aplicação usando Streamlit para gerar a estrutura front-end
"""
# FIXME: Por algum motivo o streamlit não aceita importar as páginas
# via __init__.py ou importação relativa
# pylint: disable=import-error
import streamlit as st
from introducao import intro
from questao_problema import case
from analise_geografica import geografica
from analise_prazos_x_atrasos import prazos_atrasos
from analise_tempo_operacao import tempos_operacao
from analise_valores import valores
from solucoes import solucoes
from consideracoes_finais import consideracoes_finais

# pylint: enable=import-error

PAGES = {
    "Introdução": intro,
    "Questão Problema": case,
    "Análise geográfica": geografica,
    "Análise dos Prazos e Atrasos": prazos_atrasos,
    "Análise dos Tempos de Operação": tempos_operacao,
    "Análise dos Valores dos Fretes": valores,
    "Soluções Propostas": solucoes,
    "Considerações Finais": consideracoes_finais,
}

st.sidebar.title("Índice")
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page()
