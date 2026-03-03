import streamlit as st

# Configuração da página
st.set_page_config(page_title="Governe Sua História", page_icon="👑", layout="centered")

# Estilização Personalizada (Rosa e Preto)
st.markdown("""
    <style>
    .main { background-color: #000000; color: #FFFFFF; }
    .stButton>button {
        background-color: #FF69B4;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        width: 100%;
    }
    .stButton>button:hover { background-color: #FF1493; border: none; color: white; }
    h1, h2, h3 { color: #FF69B4 !important; }
    .sidebar .sidebar-content { background-color: #1A1A1A; }
    </style>
    """, unsafe_allow_html=True)

# Menu Lateral
with st.sidebar:
    st.title("Menu")
    pagina = st.radio("Navegar para:", ["O Deserto e os Anjos", "Fale Comigo"])

if pagina == "O Deserto e os Anjos":
    st.title("O Deserto e os Anjos 🏜️✨")
    
    st.write("""
    Às vezes, a vida nos coloca em desertos onde o silêncio é ensurdecedor e a sede de propósito 
    nos faz questionar o caminho. Mas é justamente na aridez do deserto que os anjos se manifestam.
    
    Eles não vêm para tirar você do deserto antes da hora, mas para fortalecer seus passos, 
    trazer o maná da esperança e lembrar que você nunca caminha só. Cada grão de areia sob 
    seus pés é uma lição de resiliência.
    
    **Governe sua história mesmo quando o cenário for de deserto, pois é lá que sua força é forjada.**
    """)
    
    st.image("https://images.unsplash.com/photo-1473580044384-7ba9967e16a0?q=80&w=1000", caption="A força que nasce no deserto")

elif pagina == "Fale Comigo":
    st.title("Vamos Conversar? 💬")
    st.write("Se você sentiu o toque dos anjos ou precisa de uma palavra de força, clique abaixo.")

    # --- CONFIGURAÇÃO DO WHATSAPP ---
    # O número deve ter apenas dígitos: 55 (Brasil) + DDD + Número
    telefone = "5512996069640"
    texto_link = "Olá! Li seu texto sobre os Anjos e o Deserto e gostaria de conversar."
    
    # Criando o link correto
    import urllib.parse
    texto_parseado = urllib.parse.quote(texto_link)
    link_whats = f"https://wa.me/{telefone}?text={texto_parseado}"

    # Botão de redirecionamento
    st.markdown(f"""
        <a href="{link_whats}" target="_blank">
            <button style="
                background-color: #25D366;
                color: white;
                border-radius: 25px;
                border: none;
                padding: 15px 30px;
                font-weight: bold;
                font-size: 18px;
                cursor: pointer;
                width: 100%;
                display: flex;
                align-items: center;
                justify-content: center;
                text-decoration: none;
            ">
                ✅ Chamar no WhatsApp
            </button>
        </a>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("© 2026 - Governe Sua História | Desenvolvido com carinho.")
