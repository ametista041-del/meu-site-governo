import streamlit as st
from PIL import Image

# 1. CONFIGURAÇÃO DA PÁGINA (BONITA NO CELULAR)
st.set_page_config(page_title="Governe Sua História", page_icon="👑", layout="wide")

# 2. DESIGN MODO FEMININO (PRETO E ROSA CHOQUE)
st.markdown("""
<style>
    /* Fundo preto */
    .stApp {
        background-color: #000000;
    }
    
    /* Frase de topo com borda rosa suave */
    .frase-topo {
        text-align: center;
        font-size: 24px;
        font-style: italic;
        color: #FF69B4; /* Rosa Pink Suave */
        padding: 25px;
        border-bottom: 2px solid #FF1493; /* Rosa Choque */
        margin-bottom: 20px;
    }

    /* Títulos em Rosa */
    h1, h2, h3 {
        color: #FF69B4 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Textos em Branco para leitura clara */
    p, span, label, .stMarkdown {
        color: #ffffff !important;
        font-size: 18px;
    }

    /* Botão Rosa Choque arredondado */
    .stButton>button {
        background-color: #FF1493;
        color: white;
        border-radius: 20px;
        border: none;
        font-weight: bold;
        height: 3em;
        width: 100%;
    }
    
    .stButton>button:hover {
        background-color: #FF69B4;
        color: white;
        border: 1px solid white;
    }

    /* Menu Lateral com fundo escuro e borda rosa */
    [data-testid="stSidebar"] {
        background-color: #1a1a1a;
        border-right: 3px solid #FF1493;
    }
    
    /* Estilização do Formulário */
    .stForm {
        background-color: #1a1a1a;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO COM SUA FRASE DE OURO ORIGINAL
st.title("👑 Governe sua Própria História")
st.markdown('<p class="frase-topo">"Deus não me chamou para ser um cargo; Ele chamou-me de \'filhinha\'."</p>', unsafe_allow_html=True)

# 4. MENU LATERAL (NAVEGAÇÃO REAL)
st.sidebar.markdown("<h2 style='text-align: center;'>Menu Real</h2>", unsafe_allow_html=True)
cap = st.sidebar.selectbox(
    "Navegue pela minha jornada:",
    ["Identidade e Queda", "O Deserto e o Rótulo", "A Fundação Firmada", "O Governo da Nova Rota"]
)

st.write("---")

# 5. LÓGICA DAS HISTÓRIAS (SUA HISTÓRIA ORIGINAL COM TODAS AS FOTOS)
if cap == "Identidade e Queda":
    st.header("📍 Estação 1: Identidade e Valor")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try:
            # Tenta carregar a primeira foto importante
            st.image("foto.Jpg", caption="Identidade", use_container_width=True)
        except:
            st.info("Imagem de Identidade a carregar...")
            
    with col2:
        st.write("""
        Houve um tempo em que o meu valor era medido pelo que eu fazia. Enquanto eu era 'útil' para a instituição, tinha um lugar. 
        Mas, quando o meu casamento ruiu e o divórcio se tornou a minha realidade, o acolhimento deu lugar ao silêncio e ao julgamento.
        """)

elif cap == "O Deserto e o Rótulo":
    st.header("📍 Estação 2: O Momento do Vazio")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try:
            # Tenta carregar a segunda foto importante
            st.image("foto2.jpg", caption="Superação no Deserto", use_container_width=True)
        except:
            st.info("Imagem de Superação a carregar...")
            
    with col2:
        st.write("""
        Fui deixada de lado e rotulada de 'desviada' num momento em que mais precisava de colo. Ali, no vazio do abandono, 
        eu descobri que a minha fé não dependia de um desempenho, mas de uma Identidade. 
        Eu entendi que meu Pai ainda me chamava de filhinha, mesmo quando o mundo me tirava o cargo.
        """)

elif cap == "A Fundação Firmada":
    st.header("📍 Estação 3: Onde Tudo se Firmou")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try:
            # Tenta carregar a terceira foto importante
            st.image("foto3.jpg", caption="Fundação Sólida", use_container_width=True)
        except:
            st.info("Imagem de Fundação a carregar...")
            
    with col2:
        st.write("""
        Aquele deserto não foi o meu fim, foi a minha fundação. Foi onde forjei a consistência necessária para deixar de ser 
        refém das expectativas alheias e passar a governar a minha própria rota. 
        Hoje eu não ando sobre opiniões, ando sobre a Rocha que me sustentou no isolamento.
        """)

elif cap == "O Governo da Nova Rota":
    st.header("📍 Estação 4: Minha Missão e Governo")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try:
            # Tenta carregar a quarta foto importante
            st.image("foto4.jpg", caption="Assumindo o Governo", use_container_width=True)
        except:
            st.info("Imagem de Governo a carregar...")
            
    with col2:
        st.info("""
        **Missão:** Ajudar mulheres que, tal como eu, se sentem perdidas entre o que o mundo espera e o que a alma grita. 
        Aqui, não encontras apenas consolo, encontras uma bússola estratégica para o teu novo começo.
        """)
        # Adiciona balões para celebrar a missão
        if st.button("Celebrar o Governo! ✨"):
            st.balloons()

st.write("---")

# 6. SEÇÃO FIXA: O RECOMEÇO (FOTO 5)
st.subheader("💖 O Recomeço")
col_f, col_t = st.columns([1, 2])

with col_f:
    try:
        # Busca exatamente o arquivo foto5.jpg que você mostrou
        st.image("foto5.jpg", caption="Forjando um Novo Caminho", use_container_width=True)
    except:
        st.info("Aguardando upload da foto 5...")

with col_t:
    st.write("Assumindo o governo da própria rota e forjando um novo caminho. Onde o amor de Deus é o guia e você é a protagonista.")
    if st.button("Celebrar meu Novo Começo! ✨", key="botao_recomeco"):
        st.balloons()

st.write("---")

# 7. FORMULÁRIO DE CONTATO (PARA CLIENTES)
st.subheader("📩 Vamos governar juntas?")
with st.form("contato_governo"):
    nome = st.text_input("Como você se chama?")
    email = st.text_input("Seu melhor e-mail")
    interesse = st.selectbox("Em qual área você busca governo?", ["Mentoria", "Palestra", "Apoio Emocional", "Identidade"])
    mensagem = st.text_area("Conte-me brevemente o que você busca")
    
    enviar = st.form_submit_button("Enviar com Propósito")
    
    if enviar:
        if nome and email:
            st.success(f"Maravilhosa, {nome}! Recebi sua mensagem. Em breve falaremos sobre o seu governo!")
        else:
            st.error("Por favor, preencha seu nome e e-mail para eu te responder.")

st.caption("© 2026 - Governe Sua História | Design Rosa & Black")
