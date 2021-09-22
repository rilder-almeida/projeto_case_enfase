import streamlit as st


def intro():
    "Função Página introdução"
    st.title("Introdução")

    # st.markdown(
    #     """
    #     <div style="text-align: justify">

    #     </div>
    #     """,
    #     unsafe_allow_html=True,
    # )

    st.markdown(
        """
        <div style="text-align: justify">
        
        ## Sobre o Olist  - 2016/18
        O Olist não é uma empresa aventureira no segmento de e-commerce. O negócio
        é reflexo de uma década de atuação no apoio a pequenos e médios empreendedores
        a conquistarem mais clientes. Boa parte dessa experiência teve origem na Solidarium
        – empresa criada em 2007 com a missão de tornar-se o maior marketplace para
        artesãos no Brasil.
        Ao perceber que a dificuldade de acessar as grandes redes varejistas do país não
        se restringia apenas aos artesãos, o fundador do Olist, Tiago Dalvi, criou a nova
        empresa em 2015 com a missão de ajudar todo e qualquer lojista a chegar aos maiores
        e melhores marketplaces nacionais e internacionais.
        O compromisso do Olist está intimamente ligado à estruturação de um negócio sólido
        e focado na excelência de serviços prestados a lojistas e consumidores finais. Para
        isso, a aposta da empresa foi investir em um modelo de negócio sustentável e justo
        para todos os envolvidos.
        A relevância e a viabilidade da startup é reconhecida internacionalmente. O Olist
        contou com a aceleração da 500 Startups, que já ajudou a criar mais de 1500 negócios
        em 50 países. Recentemente recebeu também o aporte da Redpoint e-ventures.

        #### [Fonte](https://web.archive.org/web/20170114185412/https://olist.com/sobre-o-olist/)
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

    st.write(
        """
        <div style="text-align: justify">
        
        ## Situação da logística no Brasil

        Alguns pontos relevantes sobre a logística no Brasil durante o período:
        - 2016
            - [**O fim do e-Sedex prejudica o e-commerce**]
            (https://abcomm.org/noticias/o-fim-do-e-sedex-prejudica-o-e-commerce/)
                : "Apesar de os comentários sobre
                o fim do e-Sedex circularem há mais de um ano, a notícia, anunciada nesta
                semana, de que os Correios vão extinguir o serviço a partir de 1º de janeiro
                pegou o e-commerce de surpresa. O e-Sedex é considerado a principal alternativa
                para entrega rápida de encomendas no varejo online. Segundo estimativas da ABComm,
                o preço do frete representa de 6% a 12% do valor pago de um produto adquirido pela web.
                Quanto menor é a loja virtual, maior o peso do custo da entrega. Sem volume para
                negociar o frete com transportadoras, o preço pago pelos pequenos empresários é
                parecido com o cobrado das pessoas físicas."
            - [**Logística integrada no e-commerce**](https://www.camara-e.net/2016/12/16/logistica-integrada-no-e-commerce-o-que-uma-operacao-de-fulfillment-tem-a-ver-comigo)
                : "Segundo dados, o frete representa 62,6% dos custos logísticos do comércio
                eletrônico, enquanto armazenagem fica com 19,9% e a preparação com 17,5% dessa
                representatividade. Assim, as etapas de “order fulfillment” ou “atendimento de
                pedidos e preparação” oneram a logística do e-commerce e a preocupação que era
                voltada somente para a etapa de distribuição, agora é alimentada também pelas
                etapas iniciais que compreendem o processo de pedido, gestão do estoque, a
                coordenação dos fornecedores, separação, embalagem das mercadorias e expedição.
                Esta etapa tem consumido tempo e gerado custos significativos na logística do
                comércio eletrônico."
        - 2017
            - [**Novas oportunidades logísticas para o varejo digital**](https://www.ilos.com.br/web/e-fulfillment-novas-oportunidades-logisticas-para-o-varejo-digital/)
                : "Se a plataforma virtual oferece grande comodidade para a realização das
                vendas, os desafios logísticos da entrega física ainda são grandes
                empecilhos. Isto porque as transações comerciais podem se concretizar
                virtualmente, mas ainda é necessário guardar os produtos, administrar
                estoques e entregá-los aos clientes. O site do Mercado Livre utiliza
                já há algum tempo o Mercado Envios, a fim de facilitar alguns trâmites
                relacionados ao frete. Agora a empresa anunciou que expandirá sua atuação
                na logística, oferecendo serviço de transporte e armazenagem de produtos
                anunciados em seu site, a partir de um CD em Louveira (SP). Por enquanto,
                a operação é restrita a alguns clientes, mas há planos de expansão em breve,
                com novas instalações no Brasil."
            - [**Mercado Livre expande serviços de logística e lança fulfillment para vendedores do seu marketplace**](https://canalexecutivoblog.wordpress.com/2017/09/08/mercado-livre-expande-servicos-de-logistica-e-lanca-fulfillment-para-vendedores-do-seu-marketplace/)
                : "O objetivo da empresa com a iniciativa é garantir uma experiência
                de compra e venda ainda melhor em seu marketplace. “Para o comprador,
                o produto chegará mais rápido e embalado dentro de um padrão de qualidade
                pré-estabelecido; para o vendedor, deixar que o Mercado Livre realize
                essas etapas significa ter mais tempo para se dedicar à estratégia do
                negócio e às vendas”, destaca Leandro Bassoi, diretor do Mercado Envios."
        - 2018
            - [**Tendências de Fulfillment para marketplaces no Brasil**](https://www.ecommercebrasil.com.br/artigos/tendencias-de-fulfillment-para-marketplaces-no-brasil/)
                : "Ainda assim, existem algumas questões específicas que dividem o
                fulfillment para marketplaces em dois tipos. São eles:
                Fulfillment in house – O próprio seller define os processos,
                automações e integrações por meio de plataformas como ERP, plataformas
                de vendas em marketplace, plataformas de e-commerce e SAC.
                Fulfillment terceirizado – O seller pode contratar uma empresa especialista
                em operações logísticas e de SAC. Também pode terceirizar parte do seu
                processo de venda, focando em sua maior especialidade como varejista: comprar
                e vender. Em alguns casos, inclusive, já é possível até mesmo terceirizar
                sua operação de venda, como no caso de alguns marketplaces como Mercado Livre
                e B2W."
            - [**Pesquisa: Logística no E-commerce Brasileiro 2017**](https://www.abcomm.org/Pesquisas/Pesquisa-ABComm-Logistica-Ecommerce-2017.pdf)
        
        </div>
        <br>
        <br>
        """,
        unsafe_allow_html=True,
    )
