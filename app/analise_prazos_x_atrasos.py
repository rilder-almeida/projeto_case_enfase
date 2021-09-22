import streamlit as st

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
            "cidade_cliente",
            "estado_cliente",
            "cliente_capital",
            "regiao_cliente",
            "cidade_vendedor",
            "estado_vendedor",
            "vendedor_capital",
            "regiao_vendedor",
            "data_hora_compra",
            "data_hora_aprovacao",
            "delta_compra_aprovação",
            "data_hora_envio",
            "delta_aprovação_envio",
            "data_limite_envio",
            "delta_envio_prazo",
            "enviado_no_prazo",
            "data_hora_entrega",
            "delta_envio_entrega",
            "data_hora_previsao_entrega",
            "delta_entrega_prazo",
            "entregue_no_prazo",
        ]
    )

    st.write(df_prazos_atrasos.head())

    st.write(
        """
    (geral)
    (por estado, região)
    (por mês, ano)
    (mesmo estado, fora do estado, mesma região, fora da região)
    (capital x capital, capital x interior, interior x capital, interior x interior)


    No prazo x atrasados
    - envio do pedido
    - entrega do pedido
    - ambos
    - relação entre o atraso no envio do pedido e o atraso na entrega do pedido
    """
    )

    st.write(
        """
    #### Fontes:
        """
    )
