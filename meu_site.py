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
    h1, h2, h3 { color: #FF69B4 !important; }
    p, span, label, .stMarkdown { color: #ffffff !important; font-size: 18px; }
    
    /* Botão do WhatsApp Personalizado */
    .btn-whatsapp {
        background-color: #FF1493; color: white !important;
        padding: 15px 25px; text-decoration: none; border-radius: 30px;
        font-weight: bold; font-size: 20px; display: inline-block;
        margin-top: 20px; border: none;
    }
    .btn-whatsapp:hover { background-color: #FF69B4; color: white !important; }
</style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO
st.title("👑 Governe sua Própria História")
st.markdown('<p class="frase-topo">"Deus não me chamou para ser um cargo; Ele chamou-me de \'filhinha\'."</p>', unsafe_allow_html=True)

# 4. CONTEÚDO PRINCIPAL (HISTÓRIA E FOTOS)
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
                st.write("Houve um tempo em que o meu valor era medido pelo que eu fazia. Enquanto era 'útil', tinha um lugar. Mas no divórcio, o acolhimento deu lugar ao silêncio.")
            if cap == "Superação":
                st.write("Fui rotulada de 'desviada', mas no vazio descobri que a minha fé não dependia de um desempenho, mas de uma Identidade.")
            if cap == "Fundação":
                st.write("Aquele deserto foi a minha fundação. Forjei a consistência para deixar de ser refém de expectativas e governar a minha rota.")
            if cap == "Governo":
                st.write("Hoje ajudo mulheres que se sentem perdidas. Aqui encontras uma bússola estratégica para o teu novo começo.")
        except:
            st.error(f"Carregando {cap}...")

st.write("---")

# 5. FORMULÁRIO E CONTATO DIRECTO
col1, col2 = st.columns(2)

with col1:
    st.subheader("📩 Envie uma mensagem")
    with st.form("contato"):
        nome = st.text_input("Teu Nome:")
        mensagem = st.text_area("Como posso ajudar no teu governo?")
        enviar = st.form_submit_button("Enviar Mensagem ✨")
        if enviar:
            st.success(f"Maravilhosa, {nome}! Entrarei em contato.")

with col2:
    st.subheader("📱 Contato Imediato")
    st.write("Fale comigo agora mesmo pelo WhatsApp:")
    
    # Número atualizado: 55 (Brasil) + 12 (DDD) + número
    telefone = "5512996960696" 
    link_whatsapp = f"https://wa.me/{telefone}?text=Olá%20Adriana,%20vim%20pelo%20seu%20site%20e%20quero%20governar%20minha%20história!"
    
    st.markdown(f'<a href="{link_whatsapp}" target="_blank" class="btn-whatsapp">🟢 Chamar no WhatsApp</a>', unsafe_allow_html=True)
    st.write(f"📞 Telefone: (12) 99696-0696")

st.caption("© 2026 - Governe Sua História | Design Rosa & Black")
