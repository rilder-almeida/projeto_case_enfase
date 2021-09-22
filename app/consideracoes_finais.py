import streamlit as st


def consideracoes_finais():
    "Função página Considerações"
    st.title("Considerações")

    st.markdown(
        """
        <div style="text-align: justify">

        Primeiramente gostaria de agradecer a toda equipe da Ênfase Labs e Curso Ênfase, pela oportunidade,
        pelo processo seletivo bem elaborado e humanizado. Durante a case pude aprimorar minhas habilidades
        com as tecnologias Pandas, Numpy, Jupyter, Python, Pandas Profiling, StreamLib e dentre outras. Devido ao tempo
        limitado, não consegui imprimir os padrões de projeto possuo, tendo que focar mais na entrega do resultado
        do que na elaboração. A gestão do tempo e planejamento foram softskills que também pude praticar bastante. 
        Enfim, uma experiência interessantíssima. No mais, muito obrigado e até breve.

        Att. Rilder Almeida
            
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )
