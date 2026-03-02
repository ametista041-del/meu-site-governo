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
        <p>Aos 45 anos, minha missão não é falar sobre títulos, mas sobre recomeços. 
        Após <b>20 anos de casamento</b>, vivi o deserto da rejeição e o peso de tentar ser o que eu não era para ser aceita. Ali, no silêncio do abandono, descobri que o amor do Pai era o único padrão que eu precisava seguir.</p>
        <p>Sou <b>Graduada em Recursos Humanos</b> com formação em <b>Liderança, Mentoria e Coaching</b>. Hoje, coloco meu conhecimento e minha história à sua disposição, não como alguém que está acima, mas como alguém que caminha ao seu lado para te ajudar a governar sua própria vida.</p>
    </div>
    """, unsafe_allow_html=True)

# 4. CAPÍTULOS DA JORNADA (SENSIBILIDADE E HUMILDADE)
capitulos = {
    "Rejeição": "foto.Jpg", 
    "Libertação": "foto2.jpg", 
    "Cuidado": "foto3.jpg", 
    "Governo": "foto4.jpg"
}

cols = st.columns(len(capitulos))

for i, (cap, img_name) in enumerate(capitulos.items()):
    with cols[i]:
        st.header(cap)
        if os.path.exists(img_name):
            img = Image.open(img_name)
            st.image(img, use_container_width=True)
            
        if cap == "Rejeição":
            st.write("Por muito tempo, tentei caber em moldes que não eram meus, buscando aceitação em lugares que não me pertenciam. O divórcio revelou que eu estava tentando ser o que eu não era.")
        
        elif cap == "Libertação":
            st.write("A exaustão de manter as aparências deu lugar à liberdade de ser apenas filha. Quando parei de lutar pelo padrão humano, encontrei o descanso no amor de Deus.")
        
        elif cap == "Cuidado":
            st.write("Deus usou pessoas de onde eu menos esperava — de fora da minha bolha e de outras denominações — para me restaurar com um amor sem julgamentos. Hoje, desejo ser esse suporte para você.")
        
        elif cap == "Governo":
            st.write("Me encontrei quando entendi que só o amor do Pai basta. Se você se sente cansada de tentar se encaixar, saiba que estou aqui para te ouvir e ajudar você a retomar o governo da sua história.")

st.write("---")

# 5. CONTATO DIRETO
st.subheader("📩 Vamos conversar?")
nome = st.text_input("Como posso te chamar?")
msg = st.text_area("Me conte um pouco do que você está passando. Este é um lugar seguro.")

telefone = "5512996960696"
if nome and msg:
    texto_link = f"Olá Adriana! Sou a {nome}. {msg}".replace(" ", "%20")
    link_whats = f"https://wa.me/{telefone}?text={texto_link}"
    st.markdown(f'<a href="{link_whats}" target="_blank" class="botao-whats">💬 FALAR COM ADRIANA DE NORONHA</a>', unsafe_allow_html=True)
else:
    st.info("Sinta-se à vontade para deixar seu nome e mensagem. Responderei com todo carinho.")

st.caption("© 2026 - Governe Sua História | Adriana de Noronha")
