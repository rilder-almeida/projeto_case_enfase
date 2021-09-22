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

    st.markdown("## Onde estão os atrasos no envio?")

    st.markdown(
        """
        <div style="text-align: justify">

        #### Atraso no envio por estado do Vendedor

        - É interessante perceber menor frequência de atrasos quando enviados de MG, e maiores para o PR e SP
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

    # envio/vendedor
    df_atrasado_no_envio = df_prazos_atrasos.loc[
        df_prazos_atrasos.enviado_no_prazo == False
    ]
    dct = dict(df_atrasado_no_envio.groupby("estado_vendedor")["id_pedido"].count())
    dct = {"estados": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["estados"],
        columns=["Quantidade de pedidos atrasados no envio"],
    )
    total_pedidos_atrasados_no_envio = df_atrasado_no_envio["id_pedido"].count()

    chart_df["Quantidade de pedidos totais"] = df_prazos_atrasos.groupby(
        "estado_vendedor"
    )["id_pedido"].count()
    chart_df["Proporção de atrasos no envio"] = (
        chart_df["Quantidade de pedidos atrasados no envio"]
        / total_pedidos_atrasados_no_envio
    )
    chart_df["Proporção de pedidos totais"] = (
        df_prazos_atrasos.groupby("estado_vendedor")["id_pedido"].count()
        / df_prazos_atrasos.id_pedido.count()
    )
    chart_df.drop(
        [
            "Quantidade de pedidos atrasados no envio",
            "Quantidade de pedidos totais",
        ],
        axis=1,
        inplace=True,
    )
    with st.expander("Ver gráfico"):
        st.line_chart(chart_df)

    st.markdown(
        """
        <div style="text-align: justify">

        #### Atraso no envio por região do Vendedor

        - Observa-se que a frenquencia de atrasos no envio é proporcional ao quantidade de pedidos quando analisamos por região.
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

    df_atrasado_no_envio = df_prazos_atrasos.loc[
        df_prazos_atrasos.enviado_no_prazo == False
    ]
    dct = dict(df_atrasado_no_envio.groupby("regiao_vendedor")["id_pedido"].count())
    dct = {"regioes": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["regioes"],
        columns=["Quantidade de pedidos"],
    )
    total_pedidos_atrasados_no_envio = df_atrasado_no_envio["id_pedido"].count()
    chart_df["Proporção no atraso"] = (
        chart_df["Quantidade de pedidos"] / total_pedidos_atrasados_no_envio
    )
    chart_df["Proporção de pedidos totais"] = (
        df_prazos_atrasos.groupby("regiao_vendedor")["id_pedido"].count()
        / df_prazos_atrasos.id_pedido.count()
    )
    chart_df.drop("Quantidade de pedidos", axis=1, inplace=True)
    with st.expander("Ver gráfico"):
        st.line_chart(chart_df)

    st.markdown(
        """
        <div style="text-align: justify">

        #### Atraso no envio por motivo do Vendedor estar na capital/interior

        - Percebe-se uma maior frequêcia atraso no envio do produto quando o vendedor se encontra no interior.
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

    df_atrasado_no_envio = df_prazos_atrasos.loc[
        df_prazos_atrasos.enviado_no_prazo == False
    ]
    dct = dict(df_atrasado_no_envio.groupby("vendedor_capital")["id_pedido"].count())
    dct = {"capital": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["capital"],
        columns=["Quantidade de pedidos"],
    )
    total_pedidos_atrasados_no_envio = df_atrasado_no_envio["id_pedido"].count()
    chart_df["Proporção no atraso"] = (
        chart_df["Quantidade de pedidos"] / total_pedidos_atrasados_no_envio
    )
    chart_df["Proporção de pedidos totais"] = (
        df_prazos_atrasos.groupby("vendedor_capital")["id_pedido"].count()
        / df_prazos_atrasos.id_pedido.count()
    )
    chart_df.drop("Quantidade de pedidos", axis=1, inplace=True)
    chart_df.index = ["Interior", "Capital"]
    with st.expander("Ver gráfico"):
        st.line_chart(chart_df)

    st.markdown(
        """
        <div style="text-align: justify">

        #### Atraso no envio por estado do Cliente

        - É interessante perceber menor frequência de atrasos no envio qdo os cliente são de MG e RJ,
        em contrapartida, SP é o destino onde se encontra as maiores frequências de atraso no envio.
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

    df_atrasado_no_envio = df_prazos_atrasos.loc[
        df_prazos_atrasos.enviado_no_prazo == False
    ]
    dct = dict(df_atrasado_no_envio.groupby("estado_cliente")["id_pedido"].count())
    dct = {"estados": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["estados"],
        columns=["Quantidade de pedidos atrasados no envio"],
    )
    total_pedidos_atrasados_no_envio = df_atrasado_no_envio["id_pedido"].count()

    chart_df["Quantidade de pedidos totais"] = df_prazos_atrasos.groupby(
        "estado_cliente"
    )["id_pedido"].count()
    chart_df["Proporção entre os atrasos no envio"] = (
        chart_df["Quantidade de pedidos atrasados no envio"]
        / total_pedidos_atrasados_no_envio
    )
    chart_df["Proporção de pedidos totais"] = (
        df_prazos_atrasos.groupby("estado_cliente")["id_pedido"].count()
        / df_prazos_atrasos.id_pedido.count()
    )
    chart_df.drop(
        ["Quantidade de pedidos atrasados no envio", "Quantidade de pedidos totais"],
        axis=1,
        inplace=True,
    )
    with st.expander("Ver gráfico"):
        st.line_chart(chart_df)

    st.markdown(
        """
        <div style="text-align: justify">

        #### Atraso no envio por região do Cliente

        - Observa-se que o Sudeste é a unica região que, proporcionalmente, há atrasos no envio.
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

    df_atrasado_no_envio = df_prazos_atrasos.loc[
        df_prazos_atrasos.enviado_no_prazo == False
    ]
    dct = dict(df_atrasado_no_envio.groupby("regiao_cliente")["id_pedido"].count())
    dct = {"regioes": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["regioes"],
        columns=["Quantidade de pedidos"],
    )
    total_pedidos_atrasados_no_envio = df_atrasado_no_envio["id_pedido"].count()
    chart_df["Proporção no atraso"] = (
        chart_df["Quantidade de pedidos"] / total_pedidos_atrasados_no_envio
    )
    chart_df["Proporção de pedidos totais"] = (
        df_prazos_atrasos.groupby("regiao_cliente")["id_pedido"].count()
        / df_prazos_atrasos.id_pedido.count()
    )
    chart_df.drop("Quantidade de pedidos", axis=1, inplace=True)
    with st.expander("Ver gráfico"):
        st.line_chart(chart_df)

    st.markdown(
        """
        <div style="text-align: justify">

        #### Atraso no envio por motivo do Cliente estar na capital/interior

        - Clientes que resitem em capitais têm maior frequencia no atraso do envio por parte do vendedores.
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

    df_atrasado_no_envio = df_prazos_atrasos.loc[
        df_prazos_atrasos.enviado_no_prazo == False
    ]
    dct = dict(df_atrasado_no_envio.groupby("cliente_capital")["id_pedido"].count())
    dct = {"capital": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["capital"],
        columns=["Quantidade de pedidos"],
    )
    total_pedidos_atrasados_no_envio = df_atrasado_no_envio["id_pedido"].count()
    chart_df["Proporção no atraso"] = (
        chart_df["Quantidade de pedidos"] / total_pedidos_atrasados_no_envio
    )
    chart_df["Proporção de pedidos totais"] = (
        df_prazos_atrasos.groupby("cliente_capital")["id_pedido"].count()
        / df_prazos_atrasos.id_pedido.count()
    )
    chart_df.drop("Quantidade de pedidos", axis=1, inplace=True)
    chart_df.index = ["Interior", "Capital"]
    with st.expander("Ver gráfico"):
        st.line_chart(chart_df)

    st.markdown(
        """<br><br>
## Onde estão os atrasos na entrega?""",
        unsafe_allow_html=True,
    )

    # entrega / vendedor
    st.markdown(
        """
        <div style="text-align: justify">

        #### Atraso na entrega por estado do Vendedor

        - É interessante perceber menor frequência de atrasos na entrega, proporcionalmente, quando vindos de MG e PR.
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

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
    chart_df["Proporção de atrasos na entrega"] = (
        chart_df["Quantidade de pedidos atrasados na entrega"]
        / total_pedidos_atrasados_no_entrega
    )
    chart_df["Proporção de pedidos totais"] = (
        df_prazos_atrasos.groupby("estado_vendedor")["id_pedido"].count()
        / df_prazos_atrasos.id_pedido.count()
    )
    chart_df.drop(
        ["Quantidade de pedidos atrasados na entrega", "Quantidade de pedidos totais"],
        axis=1,
        inplace=True,
    )
    with st.expander("Ver gráfico"):
        st.line_chart(chart_df)

    st.markdown(
        """
        <div style="text-align: justify">

        #### Atraso na entrega por região do Vendedor

        - Observa-se que o Sudeste, a região que mais se originam as entregas, também apresentam o maior frequência de atrasos.
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

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
    chart_df["Proporção no atraso da entrega"] = (
        chart_df["Quantidade de pedidos"] / total_pedidos_atrasados_no_entrega
    )
    chart_df["Proporção de pedidos totais"] = (
        df_prazos_atrasos.groupby("regiao_vendedor")["id_pedido"].count()
        / df_prazos_atrasos.id_pedido.count()
    )
    chart_df.drop("Quantidade de pedidos", axis=1, inplace=True)
    with st.expander("Ver gráfico"):
        st.line_chart(chart_df)

    st.markdown(
        """
        <div style="text-align: justify">

        #### Atraso na entrega por motivo do Vendedor estar na capital/interior

        - A frequêcia atraso na entrega do produto não é intererido pelo fato do vendedor se encontrar em capitais ou interior.
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

    df_atrasado_no_entrega = df_prazos_atrasos.loc[
        df_prazos_atrasos.entregue_no_prazo == False
    ]
    dct = dict(df_atrasado_no_entrega.groupby("vendedor_capital")["id_pedido"].count())
    dct = {"capital": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["capital"],
        columns=["Quantidade de pedidos"],
    )
    total_pedidos_atrasados_no_entrega = df_atrasado_no_entrega["id_pedido"].count()
    chart_df["Proporção no atraso da entrega"] = (
        chart_df["Quantidade de pedidos"] / total_pedidos_atrasados_no_entrega
    )
    chart_df["Proporção de pedidos totais"] = (
        df_prazos_atrasos.groupby("vendedor_capital")["id_pedido"].count()
        / df_prazos_atrasos.id_pedido.count()
    )
    chart_df.drop("Quantidade de pedidos", axis=1, inplace=True)
    chart_df.index = ["Interior", "Capital"]
    with st.expander("Ver gráfico"):
        st.line_chart(chart_df)

    # entrega / cliente
    st.markdown(
        """
        <div style="text-align: justify">

        #### Atraso na entrega por estado do Cliente

        - É interessante perceber maior frequência de atrasos na entrega quando o cliente se encontra no RJ, BA, ES e AL.
        Já clientes dos estados SP e MG possuem taxas de cumprimentos de prazos exemplares.
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

    df_atrasado_no_entrega = df_prazos_atrasos.loc[
        df_prazos_atrasos.entregue_no_prazo == False
    ]
    dct = dict(df_atrasado_no_entrega.groupby("estado_cliente")["id_pedido"].count())
    dct = {"estados": list(dct.keys()), "quantidade de pedidos": list(dct.values())}
    chart_df = pd.DataFrame(
        dct["quantidade de pedidos"],
        index=dct["estados"],
        columns=["Quantidade de pedidos atrasados na entrega"],
    )
    total_pedidos_atrasados_no_entrega = df_atrasado_no_entrega["id_pedido"].count()

    chart_df["Quantidade de pedidos totais"] = df_prazos_atrasos.groupby(
        "estado_cliente"
    )["id_pedido"].count()
    chart_df["Proporção entre os atrasos na entrega"] = (
        chart_df["Quantidade de pedidos atrasados na entrega"]
        / total_pedidos_atrasados_no_entrega
    )
    chart_df["Proporção de pedidos totais"] = (
        df_prazos_atrasos.groupby("estado_cliente")["id_pedido"].count()
        / df_prazos_atrasos.id_pedido.count()
    )
    chart_df.drop(
        ["Quantidade de pedidos atrasados na entrega", "Quantidade de pedidos totais"],
        axis=1,
        inplace=True,
    )
    with st.expander("Ver gráfico"):
        st.line_chart(chart_df)

    st.markdown(
        """
        <div style="text-align: justify">

        #### Atraso na entrega por região do Cliente

        - Pode-se perceber que clientes residentes em estados no Nordeste têm maiores frequências de atraso na entrega.
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

    df_atrasado_no_entrega = df_prazos_atrasos.loc[
        df_prazos_atrasos.entregue_no_prazo == False
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
    chart_df["Proporção de pedidos totais"] = (
        df_prazos_atrasos.groupby("regiao_cliente")["id_pedido"].count()
        / df_prazos_atrasos.id_pedido.count()
    )
    chart_df.drop("Quantidade de pedidos", axis=1, inplace=True)
    with st.expander("Ver gráfico"):
        st.line_chart(chart_df)

    st.markdown(
        """
        <div style="text-align: justify">

        #### Atraso na entrega por motivo do Cliente estar na capital/interior

        - É interessante perceber maior frequência de atrasos na entrega quando o cliente se encontra em capitais.
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

    df_atrasado_no_entrega = df_prazos_atrasos.loc[
        df_prazos_atrasos.entregue_no_prazo == False
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
    chart_df["Proporção de pedidos totais"] = (
        df_prazos_atrasos.groupby("cliente_capital")["id_pedido"].count()
        / df_prazos_atrasos.id_pedido.count()
    )
    chart_df.drop("Quantidade de pedidos", axis=1, inplace=True)
    chart_df.index = ["Interior", "Capital"]
    with st.expander("Ver gráfico"):
        st.line_chart(chart_df)
