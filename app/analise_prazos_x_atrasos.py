import streamlit as st


def prazos_atrasos():
    "Função página análise prazos e atrasos"
    st.title("Análise dos prazos e atrasos")

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