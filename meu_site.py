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
    
    /* Botão de Envio para WhatsApp */
    .btn-whats-form {
        background-color: #FF1493; color: white !important;
        padding: 15px 25px; text-decoration: none; border-radius: 30px;
        font-weight: bold; font-size: 18px; display: inline-block;
        text-align: center; border: none; width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO
st.title("👑 Governe sua Própria História")
st.markdown('<p class="frase-topo">"Deus não me chamou para ser um cargo; Ele chamou-me de \'filhinha\'."</p>', unsafe_allow_html=True)

# 4. CONTEÚDO PRINCIPAL (FOTOS E CAPÍTULOS)
# Usando os nomes exatos de arquivo do seu GitHub
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
                st.write("Fui deixada de lado pelos amigos e pela igreja no momento que mais precisei.")
            elif cap == "Superação":
                st.write("Descobri que a minha fé não dependia de um desempenho, mas de uma Identidade.")
            elif cap == "Fundação":
                st.write("Aquele deserto foi a minha fundação para deixar de ser refém de expectativas.")
            elif cap == "Governo":
                st.write("Hoje ajudo mulheres a governar sua própria rota e história.")
        except:
            st.error(f"Carregando {cap}...")

st.write("---")

# 5. FORMULÁRIO COM ENVIO DIRETO PARA WHATSAPP
st.subheader("📩 Inicie seu Novo Começo")
st.write("Preencha abaixo e os dados serão enviados diretamente para o meu WhatsApp:")

nome_contato = st.text_input("Seu Nome:")
mensagem_contato = st.text_area("Como posso ajudar no seu governo?")

if st.button("Preparar Mensagem ✨"):
    if nome_contato and mensagem_contato:
        # Seu número configurado
        meu_numero = "5512996960696"
        
        # Criando o texto da mensagem
        texto_final = f"Olá Adriana! Meu nome é {nome_contato}. {mensagem_contato}"
        # Formatando para link (trocando espaços por %20)
        texto_link = texto_final.replace(" ", "%20")
        
        link_whatsapp = f"https://wa.me/{meu_numero}?text={texto_link}"
        
        st.success("Mensagem preparada com sucesso!")
        st.markdown(f'<a href="{link_whatsapp}" target="_blank" class="btn-whats-form">🟢 Enviar Agora pelo WhatsApp</a>', unsafe_allow_html=True)
    else:
        st.warning("Por favor, preencha o nome e a mensagem.")

st.caption("© 2026 - Governe Sua História | Design Rosa & Black")
