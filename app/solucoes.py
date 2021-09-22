import streamlit as st


def solucoes():
    "Função página Soluções Propostas"
    st.title("Relatório Final e Soluções Propostas")

    st.markdown(
        """
        <div style="text-align: justify">

        O Olist, mesmo sendo uma empresa com atuação nacional, foi possível perceber com base nas análises,
        a concentração de pedidos vendidos no Sudeste do país, 86.5% do total, principamente nos estados
        de São Paulo, Minas Gerais e Paraná. Já, os pedidos de compras foram feitos de forma um pouco mais
        distribuída, mas ainda sim 66.6% do total ficando nos estados de São Paulo, Rio de Janeiro e Minas Gerais.
        O que demonstra que os clientes estão mais distribuídos pelo Brasil, enquanto os vendedores estão,
        predominantemente, no Sudeste e Sul. Uma possivel solução seria focar ações de marketing concentando-se em
        estados como a Bahia, Distrito Federal e Espirito Santo, pelo fato de estarem próximos e possuirem bons mercados
        consumidores. Tanto os pedidos de compra quanto os de vendas tiveram, em sua maior parte, tiveram o fluxo do interior
        do estado de origem para o interior do estados de destino, por isso é importante focar investimentos em logística
        fora dos grandes centros para tentar proporcionar mais agilidade no processo, como formar de atração mais de parceiros
        para Olist.
        
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
        "https://github.com/rilder-almeida/projeto_case_enfase/blob/master/images/vendas2.png?raw=true"
    )

    st.markdown(
        """
        
        <div style="text-align: justify">

        Para identificar falhas e entender melhor a complexidade da logística de entregas foi realizado diversas análises cada uma das etapas:
        entre a compra e o envio, entre o envio e a entrega. Tanto por parte do comprador quanto por parte do vendedor,
        sob perpectivas de localização, como estado, região e capital/interior, parametrizados pela quantidade relativa de pedidos.<br>

        - Os estados de Minas Gerais, São Paulo e Paraná apresentaram desempenhos satisfatórios
        no envio e na entrega, assim como pelo estado de origem do vendedor e também pelo estado de destino do cliente final.
        Devendo ser estudados como forma de entender os motivos pelos quais se diferem dos demais.

        - Foi demonstrado que houveram atrasos com mais frequência na entrega quando os compradores e
        vendedores se encontram no interior de seus respectivos estados. Corroborando com o fato já apresentado anteriormente. Desta maneira, uma solução
       seria a busca de empresas de logistica terceirizadas com mais agilidade fora das capitais, como a Jadlog e a Mercado Envios, afim de reduzir esta falha de operação e 
        aumentar a qualidade do serviço prestado.

        - Entregas com destino para RJ, BA, ES e AL tiveram altas taxas de atraso, de forma incomum e preocupante.
        
        Faz-se necessário repensar se o serviço do Correios está atendendo as demandas neste locais explicitados, haja visto que nestes anos analisados
        o mesmo passou por greves e reformulou os serviços para e-commerce. Talvez a solução seja a troca de parceiros de entrega, estabelecendo contratos com
        multiplas empresas, buscando aquela que atenda melhor cada região ou estado. Outra possibilidade é a viabilização de um modelo híbrido de logística fulfillment,
        onde o Olist seria diretamente responsável por uma ou mais etapas no processo como: a entrega final ou armazenamento intermediário (hubs ou centros de distribuição)
        ou mesmo a coleta e postagem em conjunto com empresas terceirizadas.

        </div>

        """,
        unsafe_allow_html=True,
    )
