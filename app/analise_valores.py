import streamlit as st


def valores():
    "Função página análise valores dos fretes"
    st.title("Análise dos valores dos fretes")

    st.write(
        """
    (geral)
    (por estado, região)
    (por mês, ano)
    (mesmo estado, fora do estado, mesma região, fora da região)
    (capital x capital, capital x interior, interior x capital, interior x interior)


    Valores dos fretes
    -proporcao_pedido_frete x valor_total_pedido (até 100, 200, 300, 400, 500, 500+)
    """
    )

    st.write(
        """
    #### Fontes:
        """
    )
