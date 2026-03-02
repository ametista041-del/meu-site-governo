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
        Após <b>20 anos de casamento</b> e uma ruptura que me expôs ao abandono e ao silêncio institucional, decidi transformar minha dor em um porto seguro para outras mulheres.</p>
        <p>Sou <b>Graduada em Recursos Humanos</b> e possuo formação em <b>Liderança, Mentoria e Coaching</b>. Unindo minha base acadêmica à minha experiência de vida, atuo no suporte ao desenvolvimento humano e emocional, ajudando você a processar traumas e retomar o governo da sua trajetória com estratégia e empatia.</p>
        <p>Aqui, o conhecimento de nível superior encontra a autoridade de quem sobreviveu ao deserto para provar que você é capaz de reconstruir o seu destino.</p>
    </div>
    """, unsafe_allow_html=True)

# 4. CAPÍTULOS DA JORNADA
capitulos = {"Identidade": "foto.Jpg", "Superação": "foto2.jpg", "Fundação": "foto3.jpg", "Governo": "foto4.jpg"}
cols = st.columns(len(capitulos))

for i, (cap, img_name) in enumerate(capitulos.items()):
    with cols[i]:
        st.header(cap)
        try:
            img = Image.open(img_name)
            st.image(img, use_container_width=True)
            if cap == "Identidade":
                st.write("Vinte anos de história que o preconceito tentou invalidar. No divórcio, conheci o peso do julgamento, mas foi ali que decidi ser o apoio que eu não tive.")
            elif cap == "Superação":
                st.write("Onde houve abandono, encontrei a força da minha Graduação e da minha Fé. Minha formação acadêmica me deu os métodos; meu deserto me deu a escuta.")
            elif cap == "Fundação":
                st.write("Minha restauração provou que existe vida além das bolhas sociais e religiosas. Hoje, aplico minha expertise profissional para criar processos de cura e autogoverno.")
            elif cap == "Governo":
                st.write("Sou o anjo estratégico que utiliza ciência, método e vivência para te levantar. Sem filtros e sem julgamentos: seu lugar é aqui. **Governe sua história.**")
        except:
            st.error(f"Foto {cap}")

st.write("---")

# 5. CONTATO DIRETO
st.subheader("📩 Inicie seu Processo de Governo")
nome = st.text_input("Como você se chama, maravilhosa?")
msg = st.text_area("Me conte: o que você precisa restaurar e governar na sua vida hoje?")

telefone = "5512996960696"
if nome and msg:
    texto_link = f"Olá Adriana! Sou a {nome}. {msg}".replace(" ", "%20")
    link_whats = f"https://wa.me/{telefone}?text={texto_link}"
    st.markdown(f'<a href="{link_whats}" target="_blank" class="botao-whats">🚀 FALAR COM A MENTORA ADRIANA DE NORONHA</a>', unsafe_allow_html=True)
else:
    st.info("Preencha seu nome e mensagem para iniciarmos sua jornada de restauração profissional.")

st.caption("© 2026 - Governe Sua História | Adriana de Noronha")
