import streamlit as st
import pandas as pd

# import matplotlib.pyplot as plt
# import numpy as np


# FIXME: Por algum motivo o streamlit não aceita importar as páginas
# via __init__.py ou importação relativa
# pylint: disable=import-error
from core import get_dataset

# pylint: enable=import-error


def geral():
    "Função página análise geral"
    st.title("Análise dos Geral")

    df_logistica = get_dataset()

    st.markdown("###")
    # quantidade de pedidos por mes e por estado e por região, dos vendedores e dos clientes

    # estado_cliente x quantidade de pedidos
    dct = dict(df_logistica.groupby("estado_cliente")["id_pedido"].count())
    dct = {"estados": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["estados"],
        columns=["Quantidade de pedidos"],
    )
    st.bar_chart(chart_df)

    # estado_vendedor x quantidade de pedidos
    dct = dict(df_logistica.groupby("estado_vendedor")["id_pedido"].count())
    dct = {"estados": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["estados"],
        columns=["Quantidade de pedidos"],
    )
    st.bar_chart(chart_df)

    # estado_cliente x quantidade de pedidos x data_hora_compra
    serie_mes = sorted(list(df_logistica.data_hora_compra.unique()))
    list_serie = []
    for mes in serie_mes:
        df_logistica_estado = df_logistica.loc[(df_logistica.data_hora_compra == mes)]
        list_serie.append(
            dict(df_logistica_estado.groupby("estado_cliente")["id_pedido"].count())
        )
    df_estados_mes = pd.DataFrame(list_serie, index=serie_mes)
    df_estados_mes.fillna(0, inplace=True)
    st.bar_chart(df_estados_mes)

    # estado_vendedor x quantidade de pedidos x data_hora_compra
    serie_mes = sorted(list(df_logistica.data_hora_compra.unique()))
    list_serie = []
    for mes in serie_mes:
        df_logistica_estado = df_logistica.loc[(df_logistica.data_hora_compra == mes)]
        list_serie.append(
            dict(df_logistica_estado.groupby("estado_vendedor")["id_pedido"].count())
        )
    df_estados_mes = pd.DataFrame(list_serie, index=serie_mes)
    df_estados_mes.fillna(0, inplace=True)
    st.bar_chart(df_estados_mes)

    # regiao_cliente x quantidade de pedidos x data_hora_compra
    serie_mes = sorted(list(df_logistica.data_hora_compra.unique()))
    list_serie = []
    for mes in serie_mes:
        df_logistica_regiao = df_logistica.loc[(df_logistica.data_hora_compra == mes)]
        list_serie.append(
            dict(df_logistica_regiao.groupby("regiao_cliente")["id_pedido"].count())
        )
    df_regioes_mes = pd.DataFrame(list_serie, index=serie_mes)
    df_regioes_mes.fillna(0, inplace=True)
    st.bar_chart(df_regioes_mes)

    # regiao_vendedor x quantidade de pedidos x data_hora_compra
    serie_mes = sorted(list(df_logistica.data_hora_compra.unique()))
    list_serie = []
    for mes in serie_mes:
        df_logistica_regiao = df_logistica.loc[(df_logistica.data_hora_compra == mes)]
        list_serie.append(
            dict(df_logistica_regiao.groupby("regiao_vendedor")["id_pedido"].count())
        )
    df_regioes_mes = pd.DataFrame(list_serie, index=serie_mes)
    df_regioes_mes.fillna(0, inplace=True)
    st.bar_chart(df_regioes_mes)

    # cliente_capital x quantidade de pedidos x data_hora_compra
    dct = dict(df_logistica.groupby("cliente_capital")["id_pedido"].count())
    dct = {
        "cliente_capital": list(dct.keys()),
        "quantidade de pedidos": list(dct.values()),
    }
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["cliente_capital"],
        columns=["Quantidade de pedidos"],
    )
    st.bar_chart(chart_df)

    # vendedor_capital x quantidade de pedidos x data_hora_compra
    dct = dict(df_logistica.groupby("vendedor_capital")["id_pedido"].count())
    dct = {
        "vendedor_capital": list(dct.keys()),
        "quantidade de pedidos": list(dct.values()),
    }
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["vendedor_capital"],
        columns=["Quantidade de pedidos"],
    )
    st.bar_chart(chart_df)

    # cliente_capital x quantidade de pedidos x data_hora_compra
    serie_mes = sorted(list(df_logistica.data_hora_compra.unique()))
    list_serie = []
    for mes in serie_mes:
        df_logistica_capital = df_logistica.loc[(df_logistica.data_hora_compra == mes)]
        list_serie.append(
            dict(df_logistica_capital.groupby("cliente_capital")["id_pedido"].count())
        )
    df_capital_mes = pd.DataFrame(list_serie, index=serie_mes)
    df_capital_mes.fillna(0, inplace=True)
    st.bar_chart(df_capital_mes)

    # vendedor_capital x quantidade de pedidos x data_hora_compra
    serie_mes = sorted(list(df_logistica.data_hora_compra.unique()))
    list_serie = []
    for mes in serie_mes:
        df_logistica_capital = df_logistica.loc[(df_logistica.data_hora_compra == mes)]
        list_serie.append(
            dict(df_logistica_capital.groupby("vendedor_capital")["id_pedido"].count())
        )
    df_capital_mes = pd.DataFrame(list_serie, index=serie_mes)
    df_capital_mes.fillna(0, inplace=True)
    st.bar_chart(df_capital_mes)
