import streamlit as st
import pandas as pd

# import matplotlib.pyplot as plt
# import numpy as np


# FIXME: Por algum motivo o streamlit não aceita importar as páginas
# via __init__.py ou importação relativa
# pylint: disable=import-error
from core import get_dataset

# pylint: enable=import-error


def geografica():
    "Função página análise geografica"
    st.title("Análise dos geografica")

    df_geo = get_dataset(
        [
            "id_pedido",
            "data_hora_compra",
            "estado_cliente",
            "estado_vendedor",
            "regiao_cliente",
            "regiao_vendedor",
            "vendedor_capital",
            "cliente_capital",
        ]
    )

    st.markdown("##### Clientes por estado x Quantidade de pedidos")
    dct = dict(df_geo.groupby("estado_cliente")["id_pedido"].count())
    dct = {"estados": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["estados"],
        columns=["Quantidade de pedidos"],
    )
    with st.expander("Ver gráfico"):
        st.bar_chart(chart_df)

    st.markdown("##### Vendedores por estado x Quantidade de pedidos")
    dct = dict(df_geo.groupby("estado_vendedor")["id_pedido"].count())
    dct = {"estados": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["estados"],
        columns=["Quantidade de pedidos"],
    )
    with st.expander("Ver gráfico"):
        st.bar_chart(chart_df)

    st.markdown("##### Clientes por estado x Quantidade de pedidos (por mês)")
    serie_mes = sorted(list(df_geo.data_hora_compra.unique()))
    list_serie = []
    for mes in serie_mes:
        df_geo_estado = df_geo.loc[(df_geo.data_hora_compra == mes)]
        list_serie.append(
            dict(df_geo_estado.groupby("estado_cliente")["id_pedido"].count())
        )
    df_estados_mes = pd.DataFrame(list_serie, index=serie_mes)
    df_estados_mes.fillna(0, inplace=True)
    with st.expander("Ver gráfico"):
        st.bar_chart(df_estados_mes)

    st.markdown("##### Vendedores por estado x Quantidade de pedidos (por mês)")
    serie_mes = sorted(list(df_geo.data_hora_compra.unique()))
    list_serie = []
    for mes in serie_mes:
        df_geo_estado = df_geo.loc[(df_geo.data_hora_compra == mes)]
        list_serie.append(
            dict(df_geo_estado.groupby("estado_vendedor")["id_pedido"].count())
        )
    df_estados_mes = pd.DataFrame(list_serie, index=serie_mes)
    df_estados_mes.fillna(0, inplace=True)
    with st.expander("Ver gráfico"):
        st.bar_chart(df_estados_mes)

    st.markdown("##### Clientes por regiões x Quantidade de pedidos")
    dct = dict(df_geo.groupby("regiao_cliente")["id_pedido"].count())
    dct = {"regioes": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["regioes"],
        columns=["Quantidade de pedidos"],
    )
    with st.expander("Ver gráfico"):
        st.bar_chart(chart_df)

    st.markdown("##### Vendedores por regiões x Quantidade de pedidos")
    dct = dict(df_geo.groupby("regiao_vendedor")["id_pedido"].count())
    dct = {"regioes": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["regioes"],
        columns=["Quantidade de pedidos"],
    )
    with st.expander("Ver gráfico"):
        st.bar_chart(chart_df)

    st.markdown("##### Clientes por região x Quantidade de pedidos (por mês)")
    serie_mes = sorted(list(df_geo.data_hora_compra.unique()))
    list_serie = []
    for mes in serie_mes:
        df_geo_regiao = df_geo.loc[(df_geo.data_hora_compra == mes)]
        list_serie.append(
            dict(df_geo_regiao.groupby("regiao_cliente")["id_pedido"].count())
        )
    df_regioes_mes = pd.DataFrame(list_serie, index=serie_mes)
    df_regioes_mes.fillna(0, inplace=True)
    with st.expander("Ver gráfico"):
        st.bar_chart(df_regioes_mes)

    st.markdown("##### Vendedores por região x Quantidade de pedidos (por mês)")
    serie_mes = sorted(list(df_geo.data_hora_compra.unique()))
    list_serie = []
    for mes in serie_mes:
        df_geo_regiao = df_geo.loc[(df_geo.data_hora_compra == mes)]
        list_serie.append(
            dict(df_geo_regiao.groupby("regiao_vendedor")["id_pedido"].count())
        )
    df_regioes_mes = pd.DataFrame(list_serie, index=serie_mes)
    df_regioes_mes.fillna(0, inplace=True)
    with st.expander("Ver gráfico"):
        st.bar_chart(df_regioes_mes)

    st.markdown("##### Clientes na capital x Quantidade de pedidos")
    dct = dict(df_geo.groupby("cliente_capital")["id_pedido"].count())
    dct = {
        "cliente_capital": list(dct.keys()),
        "quantidade de pedidos": list(dct.values()),
    }
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["cliente_capital"],
        columns=["Quantidade de pedidos"],
    )
    with st.expander("Ver gráfico"):
        st.bar_chart(chart_df)

    st.markdown("##### Vendedores na capital x Quantidade de pedidos")
    dct = dict(df_geo.groupby("vendedor_capital")["id_pedido"].count())
    dct = {
        "vendedor_capital": list(dct.keys()),
        "quantidade de pedidos": list(dct.values()),
    }
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["vendedor_capital"],
        columns=["Quantidade de pedidos"],
    )
    with st.expander("Ver gráfico"):
        st.bar_chart(chart_df)

    st.markdown("##### Clientes na capital x Quantidade de pedidos (por mês)")
    serie_mes = sorted(list(df_geo.data_hora_compra.unique()))
    list_serie = []
    for mes in serie_mes:
        df_geo_capital = df_geo.loc[(df_geo.data_hora_compra == mes)]
        list_serie.append(
            dict(df_geo_capital.groupby("cliente_capital")["id_pedido"].count())
        )
    df_capital_mes = pd.DataFrame(list_serie, index=serie_mes)
    df_capital_mes.fillna(0, inplace=True)
    with st.expander("Ver gráfico"):
        st.bar_chart(df_capital_mes)

    st.markdown("##### Vendedores na capital x Quantidade de pedidos (por mês)")
    serie_mes = sorted(list(df_geo.data_hora_compra.unique()))
    list_serie = []
    for mes in serie_mes:
        df_geo_capital = df_geo.loc[(df_geo.data_hora_compra == mes)]
        list_serie.append(
            dict(df_geo_capital.groupby("vendedor_capital")["id_pedido"].count())
        )
    df_capital_mes = pd.DataFrame(list_serie, index=serie_mes)
    df_capital_mes.fillna(0, inplace=True)
    with st.expander("Ver gráfico"):
        st.bar_chart(df_capital_mes)
