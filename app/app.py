"""
Módulo da aplicação usando Streamlit para gerar a estrutura front-end
"""

import streamlit as st

# FIXME: Por algum motivo o streamlit não aceita importar as páginas
# via __init__.py ou importação relativa
# pylint: disable=import-error
import introducao
import questao_problema
import analise_prazos_x_atrasos
import analise_tempo_operacao
import analise_valores
import solucoes
import consideracoes_finais

# pylint: enable=import-error

# Sidebar
PAGES = {
    "Questão Problema": questao_problema.case,
    "Introdução": introducao.intro,
    "Análise dos Prazos e Atrasos": analise_prazos_x_atrasos.prazos_atrasos,
    "Análise dos Tempos de Operação": analise_tempo_operacao.tempos_operacao,
    "Análise dos Valores dos Fretes": analise_valores.valores,
    "Soluções Propostas": solucoes.solucoes,
    "Considerações Finais": consideracoes_finais.consideracoes_finais,
}

st.sidebar.title("Índice")
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page()
