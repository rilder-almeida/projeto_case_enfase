import streamlit as st


def tempos_operacao():
    "Função página análise tempos de operação"
    st.title("Análise dos tempos de operação")

    st.write(
        """
    (geral)
    (por estado, região)
    (por mês, ano)
    (mesmo estado, fora do estado, mesma região, fora da região)
    (capital x capital, capital x interior, interior x capital, interior x interior)


    Tempo médio
    - da aprovação ao envio
    - do atraso no envio
    - do envio à entrega
    - do atraso no entrega
    - da aprovação à entrega
    """
    )

    st.write(
        """
    #### Fontes:
        """
    )
