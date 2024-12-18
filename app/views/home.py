import streamlit as st
from PIL import Image


# Título e subtítulo com emojis
st.title("🎉 Comment Gauge 🎉")
st.write("### Análise de Sentimentos de Comentários no YouTube")

# Breve introdução e mensagem de boas-vindas
st.write("""
**Bem-vindo ao _Comment Gauge_** 🎬, a solução completa para obter insights precisos sobre a opinião pública em vídeos do YouTube! Nossa plataforma foi desenvolvida para ajudar **criadores de conteúdo, pesquisadores, marcas e analistas** a entenderem melhor como os espectadores estão reagindo a conteúdos específicos. Com o _Comment Gauge_, você pode transformar uma grande quantidade de dados brutos em informações valiosas que permitem tomadas de decisões mais estratégicas.
""")

tab1, tab2, tab3 = st.tabs(["Comment Gauge","Como funciona?","Sobre"])

with tab1:
    # Seções de Introdução e Funcionalidades
    st.header("💡 O que é o Comment Gauge?")
    st.write("""
    O **Comment Gauge** é uma ferramenta avançada de análise de sentimentos, projetada para simplificar o processo de coleta e análise de opiniões expressas nos comentários dos vídeos do YouTube. Por meio da nossa plataforma, você pode entender de forma rápida e precisa como os espectadores respondem a um determinado vídeo, ajudando você a ajustar estratégias, criar conteúdo mais alinhado com o público, ou até mesmo monitorar a reputação online. 

    A plataforma foi desenvolvida com foco na **facilidade de uso**, mesmo para quem não tem experiência técnica, oferecendo uma interface intuitiva que guia você passo a passo no processo de análise.
    """)

    # Lista de funcionalidades com explicações detalhadas
    st.markdown("""
    ### Funcionalidades Principais do _Comment Gauge_
    - **📥 Extrair Comentários de Vídeos do YouTube**: Não perca tempo copiando e colando comentários manualmente. Nossa ferramenta permite a extração automática de comentários de qualquer vídeo público no YouTube, facilitando a coleta de dados em grande escala.
    - **📈 Análise de Sentimentos Precisa**: Utilizamos algoritmos de Processamento de Linguagem Natural (NLP) para identificar o sentimento predominante em cada comentário, categorizando-os como **positivos**, **negativos** ou **neutros**. Isso fornece uma visão clara de como o público está reagindo ao conteúdo.
    - **📊 Visualização Detalhada de Dados**: A análise de dados é complementada com gráficos de fácil compreensão que mostram a distribuição dos sentimentos, permitindo identificar tendências e padrões. Tabelas e gráficos permitem uma análise rápida e direta dos resultados.
    - **📤 Exportar Relatórios e Compartilhar Resultados**: Ao concluir uma análise, você pode exportar um relatório completo em formato PDF, contendo todos os dados e gráficos gerados. Esses relatórios podem ser enviados por e-mail ou compartilhados com a sua equipe de forma prática.
    """)

    # Seção de Benefícios com explicações detalhadas
    st.header("🎯 Por que Usar o _Comment Gauge_?")
    st.write("""
    Se você está buscando compreender melhor o comportamento do público e melhorar suas estratégias de conteúdo, o _Comment Gauge_ oferece vantagens únicas:
    """)
    st.markdown("""
    - **🔍 Precisão na Análise**: Utilizamos algoritmos sofisticados de NLP que garantem uma análise de sentimentos precisa e confiável, com alta taxa de acerto na classificação de comentários.
    - **🖥️ Interface Intuitiva**: Nossa plataforma foi desenhada para ser simples e fácil de usar, mesmo para iniciantes. Todo o processo é guiado, desde a extração dos comentários até a geração de relatórios finais.
    - **⏰ Economia de Tempo**: A automação da coleta e análise de dados poupa um tempo significativo, que você pode usar para focar na criação de estratégias baseadas nas informações geradas.
    - **📊 Visualizações Claras e Diretas**: Gráficos e tabelas são apresentados de maneira objetiva, facilitando a interpretação dos dados e a identificação de padrões e tendências importantes.
    - **📤 Relatórios Profissionais**: Crie relatórios detalhados com todos os insights obtidos e compartilhe com colegas, clientes ou colaboradores de forma rápida e profissional.
    """)

    # FAQ ou Dúvidas Comuns com respostas mais detalhadas
    st.header("❓ Dúvidas Comuns")
    st.write("""
    Aqui estão algumas perguntas que recebemos frequentemente sobre o _Comment Gauge_:
    """)
    st.markdown("""
    **1. Quais tipos de vídeo posso analisar?**  
    Você pode analisar qualquer vídeo público disponível no YouTube, desde que tenha o ID do vídeo ou o título. A análise é feita apenas em vídeos que estejam disponíveis publicamente.

    **2. Como funciona a análise de sentimentos?**  
    Nossa ferramenta usa técnicas avançadas de Processamento de Linguagem Natural (NLP) para entender o contexto e a tonalidade dos comentários. Cada comentário é classificado como positivo, negativo ou neutro, ajudando a identificar tendências nas reações do público.

    **3. Posso salvar ou compartilhar as análises?**  
    Sim! Após realizar a análise, você pode gerar um relatório completo em PDF, contendo gráficos, tabelas e todas as informações detalhadas. Esse relatório pode ser facilmente compartilhado por e-mail ou outras plataformas de sua preferência.

    **4. A ferramenta é segura?**  
    Sim, levamos a privacidade dos dados muito a sério. Utilizamos práticas de segurança modernas para garantir que todas as informações sejam tratadas com cuidado e sigilo.
    """)

    
with tab2:
    # Seção de Como Funciona com detalhes adicionais
    st.header("⚙️ Como Funciona o _Comment Gauge_?")
    st.write("""
    O processo para realizar uma análise de sentimentos com o _Comment Gauge_ é simples e direto. Nossa ferramenta oferece diferentes formas de acessar os vídeos desejados para análise, atendendo a diversos casos de uso. Confira abaixo as opções disponíveis:
    """)
    st.markdown("""
    - 🔍 **Pesquisar por Nome**: Insira um termo de busca para procurar vídeos relacionados no YouTube. É ideal para quando você deseja analisar um vídeo, mas não sabe o ID exato.
    - 🆔 **Pesquisar por ID do Vídeo**: Para uma busca mais específica e direta, você pode inserir o ID único do vídeo do YouTube. Esta é a maneira mais rápida de acessar um vídeo quando você já sabe exatamente qual conteúdo deseja analisar.
    """)

    # Adicionando uma imagem de exemplo ou gráfico (opcional)
    # image_sentiment_llm = Image.open(r"/home/dev/Dev/AnDS/app/logo/image_sentiment_analisys.png")
    image_sentiment_llm = Image.open("app/logo/image_sentiment_analisys.png")
    st.image(image_sentiment_llm, caption="Exemplo de como a análise de sentimento e feita", use_column_width=True)

    # Seção de Exemplo de Vídeo
    st.header("📹 Exemplo de Análise de Sentimentos")
    # video_file = open(r"/home/dev/Dev/AnDS/app/midia/streamlit_video_txt.mp4", "rb")
    video_file = open("app/midia/streamlit_video_txt.mp4", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.write("""
    Para demonstrar a capacidade do _Comment Gauge_, vamos utilizar como exemplo um vídeo amplamente comentado:

    ### Vídeo Exemplo: **Trailer Oficial do Filme 'Vingadores: Ultimato'**
    - Este vídeo teve milhões de visualizações e recebeu milhares de comentários. A expectativa dos fãs e as reações à trama do filme criaram uma diversidade de opiniões que vão desde entusiastas empolgados até críticas negativas.
    - Com o _Comment Gauge_, você poderá identificar as principais emoções e sentimentos dos espectadores em relação ao trailer, visualizando comentários **positivos**, **negativos** e **neutros** de forma clara e objetiva.

    Você pode começar analisando qualquer vídeo semelhante ou utilizar um vídeo próprio para explorar as opiniões do público.
    """)
    # Seção de Tecnologia Explicada: Algoritmos LLM
    st.header("🧠 Tecnologia Por Trás do _Comment Gauge_")
    st.write("""
    O **Comment Gauge** utiliza algoritmos de ponta chamados **Modelos de Linguagem de Grande Escala (LLMs)** para realizar a análise de sentimentos dos comentários no YouTube. Esses modelos são capazes de entender o texto de maneira semelhante à humana, graças a um conjunto de técnicas avançadas. Aqui está uma explicação detalhada de como essa tecnologia funciona:
    """)

    # Explicação detalhada do funcionamento dos LLMs
    st.markdown("""
    ### Como Funcionam os LLMs?

    1. **Treinamento em Grandes Conjuntos de Dados**:
        - Um LLM é treinado utilizando uma vasta quantidade de dados textuais, que incluem livros, artigos, sites e documentos. Durante esse treinamento, o modelo aprende padrões da linguagem, como gramática, contexto e significados. Ele absorve informações sobre uma variedade de tópicos, capturando desde expressões coloquiais até termos técnicos.

    2. **Previsão de Palavras e Contexto**:
        - A parte central do aprendizado é a **previsão de palavras**. O modelo recebe sequências de texto e é treinado para prever a próxima palavra com base nas anteriores. Se houver um erro, o modelo ajusta os pesos de suas conexões neurais para melhorar suas previsões futuras. Com bilhões de exemplos, ele desenvolve a capacidade de entender o contexto de forma complexa.

    3. **Arquitetura Transformer: O Coração dos LLMs**:
        - O modelo é baseado em uma arquitetura chamada **Transformer**, que usa um mecanismo de **atenção**. Esse mecanismo permite que o LLM foque nas partes mais relevantes do texto, compreendendo relações entre palavras que estão distantes. Isso é crucial para capturar nuances e dependências de longo alcance no texto.

    4. **Processamento em Paralelo e Escalabilidade**:
        - Ao contrário de redes neurais tradicionais que processam palavras uma a uma, o Transformer permite que o modelo processe várias partes de um texto simultaneamente. Isso acelera o processamento e permite que o modelo lide com grandes volumes de dados com eficiência.

    5. **Classificação de Sentimentos com NLP**:
        - Para a análise de sentimentos, utilizamos técnicas de **Processamento de Linguagem Natural (NLP)**. O modelo analisa cada comentário e determina o sentimento predominante, categorizando-o como positivo, negativo ou neutro. Essa análise é feita considerando tanto palavras individuais quanto o contexto geral, garantindo maior precisão.

    6. **Aprendizado com Feedback Humano**:
        - Para garantir que os resultados sejam precisos, o modelo é ajustado com **Feedback Humano**. Especialistas fornecem orientações para o modelo, corrigindo erros e ajustando respostas. Isso é feito através de técnicas de aprendizado por reforço, onde o modelo aprende a refinar suas previsões a partir de exemplos corrigidos.

    ### Benefícios da Arquitetura Transformer
    - **Atenção ao Contexto**: A capacidade de focar nas partes mais relevantes de um texto permite interpretações mais precisas, especialmente quando o contexto é complexo.
    - **Escalabilidade**: Os LLMs podem ser ampliados com mais dados e parâmetros, tornando-os ainda mais poderosos e precisos.
    - **Eficiência**: A arquitetura do Transformer permite processar grandes volumes de dados rapidamente, ideal para análises em tempo real.

    ### Por Que Isso é Importante para o _Comment Gauge_?
    O uso de LLMs possibilita análises de sentimentos precisas e detalhadas, identificando nuances e tendências nos comentários dos vídeos do YouTube. Isso significa que você terá informações confiáveis e insights valiosos para ajustar suas estratégias de conteúdo, baseados em dados reais e atualizados.
    """)

with tab3:
    st.title("🎉 Sobre o Projeto Comment Gauge 🎉") 
    st.markdown("""
    ## Bem-vindo ao Comment Gauge! 🌟

    O **Comment Gauge** é uma ferramenta inteligente de análise de sentimentos focada em comentários do YouTube! Queremos ajudar você a entender a vibe geral da galera sobre qualquer assunto 🤔. Seja você criador de conteúdo, pesquisador ou parte de uma marca, temos insights valiosos para você! 📊💡

    ### Nossa Missão 🚀
    Facilitar a análise de comentários para que você possa entender o que as pessoas realmente estão dizendo — e sentindo! 😊😠😐

    ### Nossa Equipe 🧑‍💻👩‍💻
    O Comment Gauge foi desenvolvido como parte de um projeto universitário na disciplina de **Project Labs**. Nossa equipe é composta por estudantes dedicados que compartilham a paixão por tecnologia e análise de dados:

    - **Gabriel Cruz**  
    [GitHub](https://github.com/Gabriel-Cruz-Araujo) | [LinkedIn](https://www.linkedin.com/in/gabriel-cruz-711273292)
    - **Edson Augusto**  
    [GitHub](https://github.com/EdsonATB) | [LinkedIn](https://www.linkedin.com/in/edson-augusto-999a7a253/)
    - **Jefferson Andrade**  
    [GitHub](https://github.com/Jeff-Andrade) | [LinkedIn](https://www.linkedin.com/in/jefferson-andrade-429947281)
    - **Daniel Queiroz**  
    [GitHub](https://github.com/Ywinqvn) 
    - **Davi Oliveira**  
    [GitHub](https://github.com/Nyirr) 
    - **Lucas Silva**  
    [GitHub](https://github.com/LSilvaAraujo) | [LinkedIn](https://www.linkedin.com/in/lucassilvadearaujo9/)
    - **Victoria Cardoso**  
    [LinkedIn](https://www.linkedin.com/in/victoria-cardoso-chaves-leite/)
    - **Matheus Maranhão**  
    [GitHub](https://github.com/mateusmaranhao12) | [LinkedIn](https://www.linkedin.com/in/mateus-maranh%C3%A3o-24938b230?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
    - **Ikaro Petrônio**  
    [GitHub](https://github.com/ikaroPetronio) | [LinkedIn](https://www.linkedin.com/in/ikaropetroniorocha/)

    Acreditamos no poder da análise de sentimentos para transformar opiniões em insights acionáveis! 💬❤️

    ### Fale Conosco 📬
    Ficou curioso? Quer bater um papo? Estamos aqui! 😉
    - **GitHub**: (https://github.com/NxtTon/AnDS/tree/ANDS-Streamlit-API) 🚀

    Esperamos que você curta o Comment Gauge tanto quanto curtimos desenvolvê-lo! Vamos juntos explorar os sentimentos da internet! 🌐❤️
    """)
