import streamlit as st


def prazos_atrasos():
    "Função Página Análise Prazos e Atrasos"
    st.title("Análise Prazos e Atrasos - Case Data Engineering")

    st.text(
        """
[análises]
(geral)
(por estado, região)
(por mês, ano)
(mesmo estado, fora do estado, mesma região, fora da região)
(capital x capital, capital x interior, interior x capital, interior x interior)


No prazo x atrasados
- envio do pedido
- entrega do pedido
- ambos
- interferência do atraso no envio do pedido x atraso na entrega do pedido
    """
    )
