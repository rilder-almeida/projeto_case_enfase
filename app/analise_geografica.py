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
    st.title("Análise Geográfica as Vendas e Compras")

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

    st.markdown("## Onde estão as compras?")
    st.markdown(
        """
        <div style="text-align: justify">

        #### Quantidade de pedidos  de compra feitos por estado

        - Os pedidos de compras se concentram basicamente nos estados: SP (42.0%), RJ (12.8%) e MG (11.8%),
        correspondendo a 66.6% do total dos pedidos comprados.
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

    dct = dict(df_geo.groupby("estado_cliente")["id_pedido"].count())
    dct = {"estados": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["estados"],
        columns=["Quantidade de pedidos"],
    )
    with st.expander("Ver gráfico"):
        st.bar_chart(chart_df)

    st.markdown(
        """
        <div style="text-align: justify">
        <br>

        #### Quantidade de pedidos de compra por região

        - Estando presente em todas as regiões: Sudeste	(68.6%), Sul (14.3%),
        Nordeste (9.4%), Centro (5.8%), Norte (1.9%)
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

    dct = dict(df_geo.groupby("regiao_cliente")["id_pedido"].count())
    dct = {"regioes": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["regioes"],
        columns=["Quantidade de pedidos"],
    )
    with st.expander("Ver gráfico"):
        st.bar_chart(chart_df)

    st.markdown(
        """
        <div style="text-align: justify">
        <br>

        #### Quantidade de pedidos de compra em capitais

        - Os pedidos de compra se encontram majoritariamente no interior (64,1%)
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

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
        chart_df.index = ["Interior", "Capital"]
        st.bar_chart(chart_df)

    st.markdown(
        """<br><br>
## Onde estão as vendas?""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="text-align: justify">

        #### Quantidade de vendas feitos por estado

        - As vendas do Olist se concentram basicamente nos estados: SP (70.9%), MG (7.9%), PR (7.7%)
        correspondendo a 86.5% do total.
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )
    dct = dict(df_geo.groupby("estado_vendedor")["id_pedido"].count())
    dct = {"estados": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["estados"],
        columns=["Quantidade de  vendas"],
    )
    with st.expander("Ver gráfico"):
        st.bar_chart(chart_df)

    st.markdown(
        """
        <div style="text-align: justify">
        <br>

        #### Quantidade de vendas feitos por região

        - As regiões sul e sudeste são responsáveis por 96.9% do total de vendas.
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

    dct = dict(df_geo.groupby("regiao_vendedor")["id_pedido"].count())
    dct = {"regioes": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["regioes"],
        columns=["Quantidade de  vendas"],
    )
    with st.expander("Ver gráfico"):
        st.bar_chart(chart_df)

    st.markdown(
        """
        <div style="text-align: justify">
        <br>

        #### Quantidade de vendas feitos na capital

        - As vendas se encontram majoritariamente no interior (65,6%)
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

    dct = dict(df_geo.groupby("vendedor_capital")["id_pedido"].count())
    dct = {
        "vendedor_capital": list(dct.keys()),
        "quantidade de pedidos": list(dct.values()),
    }
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["vendedor_capital"],
        columns=["Quantidade de vendas"],
    )
    with st.expander("Ver gráfico"):
        chart_df.index = ["Interior", "Capital"]
        st.bar_chart(chart_df)
