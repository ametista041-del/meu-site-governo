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

# Galeria de Fotos (1 a 4)
st.markdown("## ⚔️ As Estações que Forjaram o meu Governo")
col1, col2, col3, col4 = st.columns(4)
fotos = [('foto.Jpg', 'Identidade'), ('foto2.jpg', 'Superação'), ('foto3.jpg', 'Fundação'), ('foto4.jpg', 'Governo')]
for col, (arq, cap) in zip([col1, col2, col3, col4], fotos):
    with col:
        try:
            img = Image.open(arq)
            st.image(img, caption=cap, use_container_width=True)
            if cap == "Identidade":
                st.write("""
                Houve um tempo em que o meu valor era medido pelo que eu fazia. Enquanto eu era 'útil' para a instituição, tinha um lugar. Mas, quando o meu casamento ruiu e o divórcio se tornou a minha realidade, o acolhimento deu lugar ao silêncio e ao julgamento.
                """)
            if cap == "Superação":
                st.write("""
                Fui deixada de lado e rotulada de 'desviada' num momento em que mais precisava de colo. Ali, no vazio do abandono, eu descobri que a minha fé não dependia de um desempenho, mas de uma Identidade.
                """)
            if cap == "Superação":
                st.write("""
                Fui deixada de lado e rotulada de 'desviada' num momento em que mais precisava de colo. Ali, no vazio do abandono, eu descobri que a minha fé não dependia de um desempenho, mas de uma Identidade.
                """)
        except:
            st.info(f"📷 {arq}")

st.write("---")

# FOTO 5 (RECOMEÇO) - Ajustado para foto5.jpg
col_f, col_t = st.columns([1, 2])
with col_f:
    try:
        # Tenta carregar exatamente o nome que você falou
        img_5 = Image.open('foto5.jpg')
        st.image(img_5, use_container_width=True)
    except:
        # Se não achar, tenta o outro nome comum
        try:
            img_5_alt = Image.open('foto_recomeco.jpg')
            st.image(img_5_alt, use_container_width=True)
        except:
            st.warning("📷 Salve a imagem como 'foto5.jpg' na sua pasta!")

with col_t:
    st.write("### 📖 O Recomeço e a Minha Missão")
    st.write("No vazio do abandono, eu descobri que o amor do Pai é a única Rocha inabalável.")
    st.write("Minha missão é oferecer **apoio e mentoria estratégica** para mulheres.")

st.write("---")

# FORMULÁRIO (Corrigido para evitar o NameError da sua Foto 1)
with st.form("contato"):
    nome = st.text_input("Seu nome completo:")
    whats = st.text_input("Seu WhatsApp:")
    obj = st.selectbox("Objetivo", ["Mentoria", "Apoio", "Outros"])
    enviar = st.form_submit_button("Enviar meu interesse ✨")

if enviar:
    if nome and whats:
        st.success(f"Obrigada, {nome}!")
    else:

        st.error("Preencha nome e WhatsApp.")



