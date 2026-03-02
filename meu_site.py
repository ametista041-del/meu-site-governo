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
                import streamlit as st

# --- 1. BARRA LATERAL (MENU DE NAVEGAÇÃO) ---
st.sidebar.title("Navegação")
cap = st.sidebar.selectbox(
    "Escolha o Capítulo:",
    ["Superação", "Fundação", "Governo"]
)

# --- 2. TÍTULO PRINCIPAL DO SITE ---
st.title("Meu Site - Governo")
st.write("---")

# --- 3. LOGICA DE EXIBIÇÃO DE TEXTO (TRY/EXCEPT) ---
try:
    if cap == "Superação":
        st.subheader("Fase: Superação")
        st.write("""
        Fui deixada de lado e rotulada de 'desviada' num momento em que mais precisava de colo. 
        Ali, no vazio, descobri que a minha força não dependia da aprovação de ninguém.
        """)
        # Exemplo de foto para este capítulo
        col_f, col_t = st.columns([1, 2])
        with col_f:
            st.image("foto.jpg", caption="Superação", use_container_width=True)
        with col_t:
            st.write("Aqui você pode adicionar um detalhe extra sobre a superação.")

    elif cap == "Fundação":
        st.subheader("Fase: Fundação")
        st.write("""
        Aquele deserto não foi o meu fim, foi a minha fundação. Foi onde forjei a consistência 
        necessária para deixar de ser refém das expectativas alheias e passar a governar a minha própria rota.
        """)
        # Exemplo de foto para este capítulo
        col_f, col_t = st.columns([1, 2])
        with col_f:
            st.image("foto2.jpg", caption="Fundação", use_container_width=True)
        with col_t:
            st.write("A base de tudo o que construí até hoje.")

    elif cap == "Governo":
        st.subheader("Fase: Governo")
        st.write("""
        Hoje, a minha missão é ajudar mulheres que, tal como eu, se sentem perdidas entre o que o mundo espera e o que a alma grita. 
        Aqui, não encontras apenas consolo, encontras uma bússola estratégica para o teu novo começo.
        
        **Bem-vinda ao governo da tua própria história.**
        """)
        # Exemplo de foto para este capítulo (Baseado na sua foto 5)
        col_f, col_t = st.columns([1, 2])
        with col_f:
            try:
                st.image("foto5.jpg", use_container_width=True)
            except:
                st.warning("Foto 5 não encontrada no servidor.")
        with col_t:
            st.write("**Recomeço:** O momento de assumir as rédeas.")

except Exception as e:
    st.error(f"Ocorreu um erro ao carregar os dados: {e}")

# --- 4. RODAPÉ ---
st.write("---")
st.caption("Desenvolvido para estudo de Estrutura de Dados e Streamlit - 2026")
       
                


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






