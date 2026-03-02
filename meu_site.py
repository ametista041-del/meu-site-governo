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
        <p>Aos 45 anos, sou a prova viva de que o governo da nossa história começa quando paramos de tentar caber onde não nos cabe. 
        Após <b>20 anos de casamento</b>, vivi a dor da rejeição e o peso de tentar manter padrões que não eram meus, apenas para ser aceita.</p>
        <p>Sou <b>Graduada em Recursos Humanos</b> com formação em <b>Liderança, Mentoria e Coaching</b>. Hoje, uso minha base acadêmica e minha jornada de libertação para ajudar mulheres a deixarem de ser reféns de expectativas alheias e assumirem o governo de suas vidas.</p>
    </div>
    """, unsafe_allow_html=True)

# 4. CAPÍTULOS DA JORNADA (A ESSÊNCIA)
capitulos = {"Rejeição": "foto.Jpg", "Máscaras": "foto2.jpg", "Anjos": "foto3.jpg", "Governo": "foto4.jpg"}
cols = st.columns(len(capitulos))

for i, (cap, img_name) in enumerate(capitulos.items()):
    with cols[i]:
        st.header(cap)
        try:
            img = Image.open(img_name)
            st.image(img, use_container_width=True)
            
            if cap == "Rejeição":
                st.write("Por muito tempo, tentei me encaixar em padrões que não eram meus. Vivi em ambientes que não me pertenciam, forçando uma identidade para ser aceita, até que o divórcio expôs o vazio desse esforço.")
            
            elif cap == "Máscaras":
                st.write("A exaustão de tentar ser o que eu não era me levou ao limite. O sistema religioso e social muitas vezes nos impõe um 'personagem'. Quando a máscara caiu, restou apenas eu e o Pai.")
            
            elif cap == "Anjos":
                st.write("Onde houve abandono da minha própria igreja, Deus enviou anjos improváveis. Fui curada por pessoas de outras denominações e até por quem estava fora da igreja. Ali entendi que o amor do Pai não tem fronteiras.")
            
            elif cap == "Governo":
                st.write("Encontrei-me quando entendi que só o amor de Deus basta. Hoje, uso minha graduação e minha cura para ser o anjo estratégico na sua vida. Sem máscaras, sem julgamentos. **Governe sua história.**")
        
        except:
            st.error(f"Foto {cap}")

st.write("---")

# 5. CONTATO DIRETO
st.subheader("📩 Inicie sua Jornada de Libertação")
nome = st.text_input("Qual é o seu nome, maravilhosa?")
msg = st.text_area("O que você sente que precisa 'soltar' para começar a governar hoje?")

telefone = "5512996960696"
if nome and msg:
    texto_link = f"Olá Adriana! Sou a {nome}. {msg}".replace(" ", "%20")
    link_whats = f"https://wa.me/{telefone}?text={texto_link}"
    st.markdown(f'<a href="{link_whats}" target="_blank" class="botao-whats">🚀 FALAR COM A MENTORA ADRIANA DE NORONHA</a>', unsafe_allow_html=True)
else:
    st.info("Preencha seu nome e mensagem para iniciarmos sua mentoria.")

st.caption("© 2026 - Governe Sua História | Adriana de Noronha")
