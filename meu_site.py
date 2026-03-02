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
    
    .caixa-autoridade {
        background-color: #1a1a1a; padding: 30px; border-radius: 15px;
        border-left: 8px solid #FF1493; margin-bottom: 40px;
    }
    .botao-whats {
        background-color: #FF1493; color: white !important;
        padding: 15px 25px; text-decoration: none; border-radius: 10px;
        font-weight: bold; display: block; text-align: center;
        margin-top: 20px; font-size: 20px;
    }
    .botao-whats:hover { background-color: #FF69B4; color: white !important; }
</style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO E APRESENTAÇÃO
st.title("👑 Governe sua Própria História")
st.markdown('<p class="frase-topo">"Deus não me chamou para ser um cargo; Ele chamou-me de \'filhinha\'."</p>', unsafe_allow_html=True)

with st.container():
    st.markdown(f"""
    <div class="caixa-autoridade">
        <h2>Adriana de Noronha</h2>
        <p>Aos 45 anos, minha missão é oferecer o que o sistema muitas vezes nega: um lugar de restauração real e sem julgamentos. 
        Após <b>20 anos de casamento</b> e uma ruptura que me expôs ao abandono institucional, decidi transformar minha dor em um porto seguro para outras mulheres.</p>
        <p>Sou <b>Graduada em Recursos Humanos</b> com formação em <b>Liderança, Mentoria e Coaching</b>. Unindo minha base acadêmica à minha experiência de vida, ajudo você a processar traumas e retomar o governo da sua trajetória.</p>
    </div>
    """, unsafe_allow_html=True)

# 4. CAPÍTULOS DA JORNADA (Ajustado conforme seus arquivos da foto)
# Note que foto.Jpg está com J maiúsculo como no seu GitHub
capitulos = {
    "Rejeição": "foto.Jpg", 
    "Máscaras": "foto2.jpg", 
    "Anjos": "foto3.jpg", 
    "Governo": "foto4.jpg"
}

cols = st.columns(len(capitulos))

for i, (cap, img_name) in enumerate(capitulos.items()):
    with cols[i]:
        st.header(cap)
        if os.path.exists(img_name):
            img = Image.open(img_name)
            st.image(img, use_container_width=True)
        else:
            st.warning(f"Imagem {img_name} não encontrada.")
            
        if cap == "Rejeição":
            st.write("Vinte anos de história que o preconceito tentou invalidar. No divórcio, conheci o peso do julgamento.")
        elif cap == "Máscaras":
            st.write("A exaustão de tentar ser o que eu não era. Quando a máscara caiu, restou apenas eu e o Pai.")
        elif cap == "Anjos":
            st.write("Deus enviou anjos improváveis de fora da minha bolha para me curar.")
        elif cap == "Governo":
            st.write("Sou o anjo estratégico que utiliza ciência e vivência para te levantar. Governe sua história.")

st.write("---")

# 5. CONTATO DIRETO
st.subheader("📩 Inicie seu Processo de Governo")
nome = st.text_input("Seu nome:")
msg = st.text_area("O que você precisa governar hoje?")

telefone = "5512996960696"
if nome and msg:
    texto_link = f"Olá Adriana! Sou a {nome}. {msg}".replace(" ", "%20")
    link_whats = f"https://wa.me/{telefone}?text={texto_link}"
    st.markdown(f'<a href="{link_whats}" target="_blank" class="botao-whats">🚀 FALAR COM ADRIANA DE NORONHA</a>', unsafe_allow_html=True)

st.caption("© 2026 - Governe Sua História | Adriana de Noronha")
