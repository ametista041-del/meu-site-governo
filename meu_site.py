import streamlit as st
from PIL import Image

# 1. CONFIGURAÇÃO DA PÁGINA (BONITA NO CELULAR)
st.set_page_config(page_title="Governe Sua História", page_icon="🧭", layout="wide")

# 2. DESIGN MODO FEMININO (PRETO E ROSA CHOQUE)
st.markdown("""
<style>
    .stApp { background-color: #000000; }
    .frase-topo {
        text-align: center; font-size: 24px; font-style: italic; 
        color: #FF69B4; padding: 25px; border-bottom: 2px solid #FF1493;
    }
    h1, h2, h3 { color: #FF69B4 !important; }
    p, span, label { color: #ffffff !important; font-size: 18px; }
    [data-testid="stSidebar"] { 
        background-color: #1a1a1a; 
        border-right: 3px solid #FF1493; 
    }
    .stButton>button { 
        background-color: #FF1493; color: white; border-radius: 20px; 
        width: 100%; border: none; font-weight: bold; height: 3em;
    }
    .stButton>button:hover { background-color: #FF69B4; border: 1px solid white; }
</style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO COM SUA FRASE DE OURO
st.title("🧭 Governe sua Própria História")
st.markdown('<p class="frase-topo">"Deus não me chamou para ser um cargo; Ele chamou-me de \'filhinha\'."</p>', unsafe_allow_html=True)

# 4. MENU LATERAL (NAVEGAÇÃO REAL)
st.sidebar.markdown("<h2 style='text-align: center;'>👑 Menu Real</h2>", unsafe_allow_html=True)
cap = st.sidebar.selectbox(
    "Navegue pela minha jornada:",
    ["A Queda e a Identidade", "O Deserto e o Rótulo", "A Fundação", "O Governo da Rota"]
)

st.write("---")

# 5. LÓGICA DAS HISTÓRIAS (SUA HISTÓRIA ORIGINAL AQUI)
if cap == "A Queda e a Identidade":
    st.header("📍 Identidade e Valor")
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("foto.Jpg", use_container_width=True)
        except: st.info("Espaço da Foto 1")
    with col2:
        st.write("""
        Houve um tempo em que o meu valor era medido pelo que eu fazia. Enquanto eu era 'útil' para a instituição, tinha um lugar. 
        Mas, quando o meu casamento ruiu e o divórcio se tornou a minha realidade, o acolhimento deu lugar ao silêncio e ao julgamento.
        """)

elif cap == "O Deserto e o Rótulo":
    st.header("📍 O Momento do Vazio")
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("foto2.jpg", use_container_width=True)
        except: st.info("Espaço da Foto 2")
    with col2:
        st.write("""
        Fui deixada de lado e rotulada de 'desviada' num momento em que mais precisava de colo. Ali, no vazio do abandono, 
        eu descobri que a minha fé não dependia de um desempenho, mas de uma Identidade. 
        Eu entendi que meu Pai ainda me chamava de filhinha, mesmo quando o mundo me tirava o cargo.
        """)

elif cap == "A Fundação":
    st.header("📍 Onde Tudo se Firmou")
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("foto3.jpg", use_container_width=True)
        except: st.info("Espaço da Foto 3")
    with col2:
        st.write("""
        Aquele deserto não foi o meu fim, foi a minha fundação. Foi onde forjei a consistência necessária para deixar de ser 
        refém das expectativas alheias e passar a governar a minha própria rota. 
        Hoje eu não ando sobre opiniões, ando sobre a Rocha que me sustentou no isolamento.
        """)

elif cap == "O Governo da Rota":
    st.header("📍 Minha Missão")
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            st.image("foto4.jpg", use_container_width=True)
        except: st.info("Espaço da Foto 4")
    with col2:
        st.info("""
        **Missão:** Ajudar mulheres que, tal como eu, se sentem perdidas entre o que o mundo espera e o que a alma grita. 
        Aqui, não encontras apenas consolo, encontras uma bússola estratégica para o teu novo começo.
        """)
        st.balloons()

st.write("---")

# 6. SEÇÃO RECOMEÇO (FOTO 5)
col_f, col_t = st.columns([1, 2])
with col_f:
    try:
        st.image("foto5.jpg", use_container_width=True)
    except: st.info("Foto do Recomeço")
with col_t:
    st.subheader("💖 O Recomeço")
    st.write("Assumindo o governo da própria rota. Clique abaixo para celebrar!")
    if st.button("Celebrar meu Novo Começo! ✨"):
        st.balloons()

st.write("---")

# 7. FORMULÁRIO DE CONTATO (PARA CLIENTES)
st.subheader("📩 Vamos conversar?")
with st.form("contato_cliente"):
    nome = st.text_input("Qual o seu nome?")
    email = st.text_input("Seu melhor e-mail")
    ajuda = st.selectbox("Como posso te ajudar?", ["Mentoria", "Palestra", "Apoio Emocional"])
    mensagem = st.text_area("Conte um pouco da sua história para mim")
    
    enviar = st.form_submit_button("Enviar Mensagem")
    if enviar:
        if nome and email:
            st.success(f"Obrigada, {nome}! Recebi sua mensagem e entrarei em contato em breve.")
        else:
            st.error("Por favor, preencha nome e e-mail.")

st.caption("© 2026 - Governe Sua História | Design Rosa & Black")
