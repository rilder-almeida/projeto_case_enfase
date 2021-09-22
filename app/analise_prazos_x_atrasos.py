import streamlit as st
import pandas as pd

# FIXME: Por algum motivo o streamlit não aceita importar as páginas
# via __init__.py ou importação relativa
# pylint: disable=import-error
from core import get_dataset

# pylint: enable=import-error


def prazos_atrasos():
    "Função página análise prazos e atrasos"
    st.title("Análise dos prazos e atrasos")

    df_prazos_atrasos = get_dataset(
        [
            "id_pedido",
            "estado_cliente",
            "cliente_capital",
            "regiao_cliente",
            "estado_vendedor",
            "vendedor_capital",
            "regiao_vendedor",
            "enviado_no_prazo",
            "entregue_no_prazo",
        ]
    )

    # entrega / vendedor
    df_atrasado_no_entrega = df_prazos_atrasos.loc[
        df_prazos_atrasos.entregue_no_prazo == False
    ]
    dct = dict(df_atrasado_no_entrega.groupby("estado_vendedor")["id_pedido"].count())
    dct = {"estados": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["estados"],
        columns=["Quantidade de pedidos atrasados na entrega"],
    )
    total_pedidos_atrasados_no_entrega = df_atrasado_no_entrega["id_pedido"].count()

    chart_df["Quantidade de pedidos totais"] = df_prazos_atrasos.groupby(
        "estado_vendedor"
    )["id_pedido"].count()
    chart_df["Proporção entre os atrasos na entrega"] = (
        chart_df["Quantidade de pedidos atrasados na entrega"]
        / total_pedidos_atrasados_no_entrega
    )
    chart_df.drop(
        ["Quantidade de pedidos atrasados na entrega", "Quantidade de pedidos totais"],
        axis=1,
        inplace=True,
    )
    st.line_chart(chart_df)

    df_atrasado_no_entrega = df_prazos_atrasos.loc[
        df_prazos_atrasos.entregue_no_prazo == False
    ]
    dct = dict(df_atrasado_no_entrega.groupby("regiao_vendedor")["id_pedido"].count())
    dct = {"regioes": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["regioes"],
        columns=["Quantidade de pedidos"],
    )
    total_pedidos_atrasados_no_entrega = df_atrasado_no_entrega["id_pedido"].count()
    chart_df["Proporção no atraso"] = (
        chart_df["Quantidade de pedidos"] / total_pedidos_atrasados_no_entrega
    )
    chart_df.drop("Quantidade de pedidos", axis=1, inplace=True)
    st.line_chart(chart_df)

    df_atrasado_no_entrega = df_atrasado_no_entrega.loc[
        df_atrasado_no_entrega.entregue_no_prazo == False
    ]
    dct = dict(df_atrasado_no_entrega.groupby("vendedor_capital")["id_pedido"].count())
    dct = {"capital": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["capital"],
        columns=["Quantidade de pedidos"],
    )
    total_pedidos_atrasados_no_entrega = df_atrasado_no_entrega["id_pedido"].count()
    chart_df["Proporção no atraso"] = (
        chart_df["Quantidade de pedidos"] / total_pedidos_atrasados_no_entrega
    )
    chart_df.drop("Quantidade de pedidos", axis=1, inplace=True)
    chart_df.index = ["Interior", "Capital"]
    st.bar_chart(chart_df)

    # entrega / cliente
    df_atrasado_no_entrega = df_atrasado_no_entrega.loc[
        df_atrasado_no_entrega.entregue_no_prazo == False
    ]
    dct = dict(df_atrasado_no_entrega.groupby("estado_cliente")["id_pedido"].count())
    dct = {"estados": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["estados"],
        columns=["Quantidade de pedidos atrasados na entrega"],
    )
    total_pedidos_atrasados_no_entrega = df_atrasado_no_entrega["id_pedido"].count()

    chart_df["Quantidade de pedidos totais"] = df_atrasado_no_entrega.groupby(
        "estado_cliente"
    )["id_pedido"].count()
    chart_df["Proporção entre os atrasos na entrega"] = (
        chart_df["Quantidade de pedidos atrasados na entrega"]
        / total_pedidos_atrasados_no_entrega
    )

    chart_df.drop(
        ["Quantidade de pedidos atrasados na entrega", "Quantidade de pedidos totais"],
        axis=1,
        inplace=True,
    )
    st.line_chart(chart_df)

    df_atrasado_no_entrega = df_atrasado_no_entrega.loc[
        df_atrasado_no_entrega.entregue_no_prazo == False
    ]
    dct = dict(df_atrasado_no_entrega.groupby("regiao_cliente")["id_pedido"].count())
    dct = {"regioes": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["regioes"],
        columns=["Quantidade de pedidos"],
    )
    total_pedidos_atrasados_no_entrega = df_atrasado_no_entrega["id_pedido"].count()
    chart_df["Proporção no atraso"] = (
        chart_df["Quantidade de pedidos"] / total_pedidos_atrasados_no_entrega
    )

    chart_df.drop("Quantidade de pedidos", axis=1, inplace=True)
    st.line_chart(chart_df)

    df_atrasado_no_entrega = df_atrasado_no_entrega.loc[
        df_atrasado_no_entrega.entregue_no_prazo == False
    ]
    dct = dict(df_atrasado_no_entrega.groupby("cliente_capital")["id_pedido"].count())
    dct = {"capital": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["capital"],
        columns=["Quantidade de pedidos"],
    )
    total_pedidos_atrasados_no_entrega = df_atrasado_no_entrega["id_pedido"].count()
    chart_df["Proporção no atraso"] = (
        chart_df["Quantidade de pedidos"] / total_pedidos_atrasados_no_entrega
    )

    chart_df.drop("Quantidade de pedidos", axis=1, inplace=True)
    chart_df.index = ["Interior", "Capital"]
    st.bar_chart(chart_df)
