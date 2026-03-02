import streamlit as st
import os
from PIL import Image

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Governe Sua História", page_icon="👑", layout="wide")

# 2. DESIGN PERSONALIZADO (PRETO E ROSA CHOQUE)
st.markdown("""
<style>
    .stApp { background-color: #000000; }
    .frase-topo {
        text-align: center; font-size: 26px; font-style: italic;
        color: #FF69B4; padding: 30px; border-bottom: 2px solid #FF1493;
        margin-bottom: 25px; font-family: 'Georgia', serif;
    }
    h1, h2, h3 { color: #FF69B4 !important; font-family: 'Georgia', serif; }
    p, span, label, .stMarkdown { color: #ffffff !important; font-size: 18px; line-height: 1.6; }
    
    /* Botão Rosa de Envio */
    .botao-whats {
        background-color: #FF1493;
        color: white !important;
        padding: 15px 25px;
        text-decoration: none;
        border-radius: 10px;
        font-weight: bold;
        display: block;
        text-align: center;
        margin-top: 20px;
        font-size: 20px;
    }
    .botao-whats:hover { background-color: #FF69B4; }
</style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO
st.title("👑 Governe sua Própria História")
st.markdown('<p class="frase-topo">"Deus não me chamou para ser um cargo; Ele chamou-me de \'filhinha\'."</p>', unsafe_allow_html=True)

# 4. CONTEÚDO PRINCIPAL (HISTÓRIA COMPLETA COM OS ANJOS)
capitulos = {
    "Identidade": "foto.Jpg",
    "Superação": "foto2.jpg",
    "Fundação": "foto3.jpg",
    "Governo": "foto4.jpg"
}

cols = st.columns(len(capitulos))

for i, (cap, img_name) in enumerate(capitulos.items()):
    with cols[i]:
        st.header(cap)
        try:
            img = Image.open(img_name)
            st.image(img, use_container_width=True)
            
            if cap == "Identidade":
                st.write("""Houve um tempo em que o meu valor era medido pelo que eu fazia. Enquanto eu era 'útil' para a instituição, tinha um lugar. Mas, quando o meu casamento ruiu e o divórcio se tornou a minha realidade, o acolhimento deu lugar ao silêncio e ao julgamento.""")
            
            elif cap == "Superação":
                st.write("""Fui deixada de lado e rotulada de 'desviada' num momento em que mais precisava de colo. Ali, no vazio do abandono, eu descobri que a minha fé não dependia de um desempenho, mas de uma Identidade que nada pode abalar.""")
            
            elif cap == "Fundação":
                st.write("""Aquele deserto não foi o meu fim, foi a minha fundação. Foi onde forjei a consistência necessária para deixar de ser refém das expectativas alheias e passar a governar a minha própria rota com autoridade.""")
            
            elif cap == "Governo":
                st.write("""Nos meus dias mais escuros, Deus enviou **anjos** que me estenderam a mão quando eu não tinha forças. Hoje, a minha missão é retribuir: eu decidi que quero ser também um **anjo na vida de alguém**. Se te sentes perdida, aqui encontras uma bússola estratégica e o apoio para o teu novo começo. **Bem-vinda ao teu governo.**""")

        except:
            st.error(f"Carregando {cap}...")

st.write("---")

# 5. FORMULÁRIO E WHATSAPP DIRETO
col_f, col_esp = st.columns([2, 1])

with col_f:
    st.subheader("📩 Inicie seu Novo Começo")
    nome = st.text_input("Qual é o seu nome, maravilhosa?")
    msg = st.text_area("O que a sua alma grita hoje? Compartilhe comigo.")

    # Link dinâmico do WhatsApp (Número: 5512996960696)
    telefone = "5512996960696"
    if nome and msg:
        texto_link = f"Olá Adriana! Sou a {nome}. {msg}".replace(" ", "%20")
        link_whats = f"https://wa.me/{telefone}?text={texto_link}"
        st.markdown(f'<a href="{link_whats}" target="_blank" class="botao-whats">🚀 ENVIAR PARA O WHATSAPP DA ADRIANA</a>', unsafe_allow_html=True)
    else:
        st.info("Preencha seu nome e mensagem acima para liberar o botão de envio direto para o meu WhatsApp.")

st.caption("© 2026 - Governe Sua História | Adriana")
