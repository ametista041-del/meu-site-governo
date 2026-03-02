import streamlit as st
from PIL import Image

# 1. Configuração da página
st.set_page_config(page_title="Governe Sua História", page_icon="🧭", layout="wide")

# --- 2. DESIGN MODO ESCURO (TELA PRETA) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    .frase-topo {
        text-align: center; font-size: 28px; font-style: italic; color: #ffffff;
        padding: 35px; border-bottom: 2px solid #333;
    }
    .stMarkdown, div[data-testid="stVerticalBlock"] > div:has(div.stMarkdown) {
        background-color: #1a1a1a; padding: 25px; border-radius: 15px;
    }
    h1, h2, h3, p, span, label { color: #ffffff !important; }
    [data-testid="stForm"] { background-color: #1a1a1a; padding: 30px; border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CONTEÚDO ---
st.title("🧭 Governe sua Própria História")
st.markdown('<p class="frase-topo">"O Amor de Deus não nos mede pelo que fazemos, mas nos acolhe pelo que somos: Suas filhinhas."</p>', unsafe_allow_html=True)
import streamlit as st
# --- 1. GALERIA DE FOTOS (LINHA 27 EM DIANTE) ---
st.markdown("## 🗺️ As Estações que Forjaram o meu Governo")
coll, col2, col3, col4 = st.columns(4)

# Lista com os arquivos e os títulos das colunas
fotos = [
    ('foto.Jpg', 'Identidade'), 
    ('foto2.jpg', 'Superação'), 
    ('foto3.jpg', 'Fundação'), 
    ('foto4.jpg', 'Governo')
]

for col, (arq, nome_cap) in zip([coll, col2, col3, col4], fotos):
    with col:
        try:
            st.image(arq, caption=nome_cap, use_container_width=True)
        except:
            st.warning(f"Erro ao abrir {arq}")

st.write("---")

# --- 2. BARRA LATERAL (MENU DE NAVEGAÇÃO) ---
st.sidebar.title("Navegação")
cap = st.sidebar.selectbox(
    "Escolha o Capítulo:",
    ["Identidade", "Superação", "Fundação", "Governo"]
)

# --- 3. TÍTULO DINÂMICO E CONTEÚDO ---
st.title(f"Capítulo: {cap}")

if cap == "Identidade":
    st.write("""
    Houve um tempo em que o meu valor era medido pelo que eu fazia. 
    Enquanto eu era 'útil' para a instituição, tinha um lugar.
    """)

elif cap == "Superação":
    st.write("""
    Fui deixada de lado e rotulada de 'desviada' num momento em que mais precisava de colo. 
    Ali, no vazio, descobri que a minha força não dependia da aprovação de ninguém.
    """)

elif cap == "Fundação":
    st.write("""
    Aquele deserto não foi o meu fim, foi a minha fundação. Foi onde forjei a consistência 
    necessária para deixar de ser refém das expectativas alheias.
    """)

elif cap == "Governo":
    st.write("""
    Hoje, a minha missão é ajudar mulheres que, tal como eu, se sentem perdidas entre o que o mundo espera e o que a alma grita. 
    **Bem-vinda ao governo da tua própria história.**
    """)

st.write("---")

# --- 4. SEÇÃO DE DESTAQUE FINAL ---
col_f, col_t = st.columns([1, 2])
with col_f:
    try:
        st.image("foto5.jpg", use_container_width=True)
    except:
        st.info("Foto 5 (Recomeço) não encontrada.")
with col_t:
    st.subheader("O Recomeço")
    st.write("Assumindo o governo da própria rota e forjando um novo caminho.")

