import streamlit as st


def case():
    "Função Página Questão Problema"
    st.title("Case Data Engineering - Curso Ênfase")

    st.markdown(
        """
        <div style="text-align: justify">

        ## Questão problema
        O Olist é a maior loja de departamento presente nos principais marketplaces de
        destaque no Brasil, como o Zoom, Shoptime, Carrefour, Americanas e outros. Os produtos
        listados pela empresa são vendidos e entregues por lojistas de todo o Brasil, os quais são
        cuidadosamente selecionados e aprovados em um processo criterioso.
        Para os lojistas, a grande vantagem é a possibilidade de vender seus produtos sem muita
        ‘dor de cabeça’ com um contrato simples. Após a compra de um produto através do Olist,
        o vendedor recebe uma notificação para começar a processar o pedido e o cliente recebe
        uma estimativa de data de entrega. Possivelmente, nem todas as decisões da empresa foram
        acertadas no quesito de carteira de produtos e profitabilidade.
        Apresente uma análise das vendas da empresa, baseando-se nos dados presentes no dataset,
        e a partir dela proponha um plano de ação para melhorar os resultados da empresa. Este
        plano pode ser na linha de logística, marketing, vendas, produtos, entre outros.
                
        </div>
        <br>

        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="text-align: justify">

        ## Objetivo
        Este projeto tem como objetivo a análise das vendas da Olist no período entre
        2016 e 2018. O estudo destas vendas foi realizado sob a ótica das operações logísticas da empresa,
        desde o ato da compra até a entrega, em séries geográficas, quantitativas e relativas. Tendo como intúito
        identificar possíveis falhas ou deficiências nos processos, de forma a propor
        soluções eficientes que impactem no positivamente na resultados do negócio.

        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="text-align: justify">

        ## Etapas
        Para melhor execução, o projeto foi dividido da seguinte maneira:
        - Entendimento do negócio, mercado de atuação, público alvo, serviços e produtos ofertados;
        - Análise dos datasets, colunas, relações e tipagem;
        - Realização da extração, limpeza, conversão, validação e tratamento dos dados;
        - Produção do dataset de logística, unificado e condizente com as demandas do projeto;
        - Planejamento das questões abordadas durante a análise para obtenção dos resultados;
        - Preparo da estrutura da aplicação de visualização do projeto;
        - Elaboração dos gráficos e tabelas relacionadas às necessidades da análise;
        - Inferência de resultados baseando-se nos dados e conhecimentos complementares;
        - Análise dos resultados, levantamento de soluções e propostas;
        - Deployment da aplicação, repositório e documentações.
        
        </div>
        """,
        unsafe_allow_html=True,
    )
