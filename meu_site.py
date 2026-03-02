import streamlit as st
from PIL import Image

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Governe Sua História", page_icon="👑", layout="wide")

# 2. DESIGN PERSONALIZADO (ROSA E PRETO)
st.markdown("""
<style>
    /* Fundo principal preto */
    .stApp {
        background-color: #000000;
    }
    
    /* Estilização da frase de topo com borda rosa */
    .frase-topo {
        text-align: center;
        font-size: 26px;
        font-style: italic;
        color: #FF69B4; /* Rosa Choque Suave */
        padding: 30px;
        border-bottom: 2px solid #FF1493;
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
    }

    /* Botão e campos do formulário com detalhes em rosa */
    .stButton>button {
        background-color: #FF1493;
        color: white;
        border-radius: 20px;
        border: none;
        width: 100%;
    }
    
    .stButton>button:hover {
        background-color: #FF69B4;
        color: white;
    }

    /* Menu Lateral */
    [data-testid="stSidebar"] {
        background-color: #1a1a1a;
        border-right: 2px solid #FF1493;
    }
</style>
""", unsafe_allow_html=True)

# 3. CONTEÚDO INICIAL
st.title("👑 Governe sua Própria História")
st.markdown('<p class="frase-topo">"O Amor de Deus não nos mede pelo que fazemos, mas nos acolhe pelo que somos."</p>', unsafe_allow_html=True)

# 4. GALERIA DE FOTOS (ESTAÇÕES)
st.markdown("### 🌸 As Estações do seu Florescer")
coll, col2, col3, col4 = st.columns(4)

fotos_galeria = [
    ('foto.Jpg', 'Identidade'), 
    ('foto2.jpg', 'Superação'), 
    ('foto3.jpg', 'Fundação'), 
    ('foto4.jpg', 'Governo')
]

for col, (arq, nome_cap) in zip([coll, col2, col3, col4], fotos_galeria):
    with col:
        try:
            img = Image.open(arq)
            st.image(img, caption=nome_cap, use_container_width=True)
        except:
            st.info(f"Carregando {nome_cap}...")

st.write("---")

# 5. MENU DE NAVEGAÇÃO LATERAL
st.sidebar.markdown("<h2 style='text-align: center;'>Menu Real</h2>", unsafe_allow_html=True)
cap = st.sidebar.selectbox(
    "Para onde vamos agora?",
    ["Identidade", "Superação", "Fundação", "Governo"]
)

# 6. EXIBIÇÃO DO CONTEÚDO (CONFORME O MENU)
st.subheader(f"📍 Você está em: {cap}")

if cap == "Identidade":
    st.write("Sua essência é única. Aqui começa a descoberta de quem você realmente é, além dos rótulos.")
elif cap == "Superação":
    st.write("As cicatrizes são marcas de vitória. Você não é o que te aconteceu, você é o que escolheu se tornar.")
elif cap == "Fundação":
    st.write("Construindo sobre a rocha. Firmando os pés para que nada te abale.")
elif cap == "Governo":
    st.write("Assuma o cetro da sua vida. Você foi chamada para governar sua rota com sabedoria.")

st.write("---")

# 7. SEÇÃO RECOMEÇO (FOTO 5)
col_f, col_t = st.columns([1, 2])
with col_f:
    try:
        st.image("foto5.jpg", use_container_width=True)
    except:
        st.info("Sua foto de recomeço aparecerá aqui.")
with col_t:
    st.subheader("💖 O Novo Começo")
    st.write("Cada passo que você dá agora é escrito por você e por Deus. Sinta a liberdade de ser quem você nasceu para ser.")

st.write("---")

# 8. FORMULÁRIO DE CONTATO PARA CLIENTES
with st.container():
    st.subheader("📩 Vamos conversar?")
    with st.form("contato_mulher"):
        nome = st.text_input("Como você se chama?")
        email = st.text_input("Seu melhor e-mail")
        interesse = st.multiselect("No que você busca governo hoje?", ["Emocional", "Profissional", "Espiritual", "Relacionamentos"])
        mensagem = st.text_area("Deixe sua mensagem para mim")
        
        enviar = st.form_submit_button("Enviar com Amor")
        
        if enviar:
            if nome and email:
                st.success(f"Maravilhosa! Recebi seu contato, {nome}. Logo falaremos!")
            else:
                st.error("Por favor, preencha seu nome e e-mail para eu te responder.")

st.caption("© 2026 - Governe Sua História | Design Feminino")
