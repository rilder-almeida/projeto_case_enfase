import streamlit as st


def solucoes():
    "Função página Soluções Propostas"
    st.title("Relatório Final e Soluções Propostas")

    st.markdown(
        """
        <div style="text-align: justify">

        O Olist, mesmo sendo uma empresa com atuação nacional, foi possivel perceber com base nas vendas
        a concentração de vendas no Sudeste do país, 86.5% do total, principamente nos estados
        de São Paulo, Minas Gerais e Paraná. Já, os pedidos de compras foram feitos de forma um pouco mais
        distribuída, mas ainda sim, 66,6% do total ficando nos estados de São Paulo, Rio de Janeiro e Minas Gerais.
        </div>
        """,
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns(2)

    col1.subheader("Pedidos Comprados")
    col1.image(
        "https://github.com/rilder-almeida/projeto_case_enfase/blob/master/images/compras.png?raw=true"
    )

    col2.subheader("Pedidos Vendidos")
    col2.image(
        "https://github.com/rilder-almeida/projeto_case_enfase/blob/master/images/vendas.png?raw=true"
    )
