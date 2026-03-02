import streamlit as st
import urllib.parse

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Governe Sua História", page_icon="👑", layout="wide")

# 2. DESIGN MODO FEMININO (PRETO E ROSA CHOQUE)
st.markdown("""
<style>
    .stApp { background-color: #000000; }
    .frase-topo {
        text-align: center; font-size: 24px; font-style: italic; 
        color: #FF69B4; padding: 25px; border-bottom: 2px solid #FF1493;
    }
    h1, h2, h3 { color: #FF69B4 !important; }
    p, span, label, .stMarkdown { color: #ffffff !important; font-size: 18px; }
    .stButton>button { 
        background-color: #FF1493; color: white; border-radius: 20px; 
        width: 100%; border: none; font-weight: bold; height: 3em;
    }
    .stButton>button:hover { background-color: #FF69B4; border: 1px solid white; }
    [data-testid="stSidebar"] { background-color: #1a1a1a; border-right: 3px solid #FF1493; }
</style>
""", unsafe_allow_html=True)

# 3. CABEÇALHO
st.title("👑 Governe sua Própria História")
st.markdown('<p class="frase-topo">"Deus não me chamou para ser um cargo; Ele chamou-me de \'filhinha\'."</p>', unsafe_allow_html=True)

# 4. MENU LATERAL
st.sidebar.markdown("<h2 style='text-align: center;'>Menu Real</h2>", unsafe_allow_html=True)
cap = st.sidebar.selectbox(
    "Navegue pela minha jornada:",
    ["Identidade e Queda", "O Deserto e os Anjos", "A Fundação Firmada", "O Governo da Nova Rota"]
)

st.write("---")

# 5. CONTEÚDO DINÂMICO (HISTÓRIA COMPLETA)
if cap == "Identidade e Queda":
    st.header("📍 Estação 1: Identidade e Valor")
    col1, col2 = st.columns([1, 2])
    with col1:
        try: st.image("foto.Jpg", use_container_width=True)
        except: st.info("Imagem 1 carregando...")
    with col2:
        st.write("""
        Houve um tempo em que o meu valor era medido pelo que eu fazia. Enquanto eu era 'útil' para a instituição, tinha um lugar. 
        Mas, quando o meu casamento ruiu e o divórcio se tornou a minha realidade, o acolhimento deu lugar ao silêncio e ao julgamento.
        """)

elif cap == "O Deserto e os Anjos":
    st.header("📍 Estação 2: O Momento do Vazio e os Anjos")
    col1, col2 = st.columns([1, 2])
    with col1:
        try: st.image("foto2.jpg", use_container_width=True)
        except: st.info("Imagem 2 carregando...")
    with col2:
        st.write("""
        Fui deixada de lado e rotulada de 'desviada' num momento em que mais precisava de colo. Ali, no vazio do abandono, 
        descobri que a minha fé não dependia de um desempenho, mas de uma Identidade. 
        
        Nesse deserto, Deus me mostrou que existem **anjos nesta terra**: pessoas que, muitas vezes, nem estão dentro de uma igreja, 
        mas que se tornaram a própria 'Igreja' para mim. Elas me estenderam a mão sem julgar. 
        Hoje, minha missão é ser uma inspiração para outras mulheres, retribuindo o amor e a força que essas pessoas me deram.
        """)

elif cap == "A Fundação Firmada":
    st.header("📍 Estação 3: Onde Tudo se Firmou")
    col1, col2 = st.columns([1, 2])
    with col1:
        try: st.image("foto3.jpg", use_container_width=True)
        except: st.info("Imagem 3 carregando...")
    with col2:
        st.write("""
        Aquele deserto não foi o meu fim, foi a minha fundação. Foi onde forjei a consistência necessária para deixar de ser 
        refém das expectativas alheias e passar a governar a minha própria rota. 
        Hoje eu não ando sobre opiniões, ando sobre a Rocha que me sustentou no isolamento.
        """)

elif cap == "O Governo da Nova Rota":
    st.header("📍 Estação 4: Minha Missão")
    col1, col2 = st.columns([1, 2])
    with col1:
        try: st.image("foto4.jpg", use_container_width=True)
        except: st.info("Imagem 4 carregando...")
    with col2:
        st.info("""
        **Missão:** Ajudar mulheres que, tal como eu, se sentem perdidas entre o que o mundo espera e o que a alma grita. 
        Aqui, não encontras apenas consolo, encontras uma bússola estratégica para o teu novo começo.
        """)

st.write("---")

# 6. SEÇÃO FIXA: O RECOMEÇO
col_f, col_t = st.columns([1, 2])
with col_f:
    try: st.image("foto5.jpg", use_container_width=True)
    except: st.info("Foto 5 carregando...")
with col_t:
    st.subheader("💖 O Recomeço")
    st.write("Assumindo o governo da própria rota e forjando um novo caminho.")

st.write("---")

# 7. FORMULÁRIO COM CONEXÃO PARA WHATSAPP
st.subheader("📩 Vamos governar juntas?")
with st.form("contato_whatsapp"):
    nome = st.text_input("Qual o seu nome?")
    ajuda = st.selectbox("Como posso te ajudar?", ["Mentoria", "Palestra", "Apoio Emocional", "Identidade"])
    mensagem_extra = st.text_area("Conte-me um pouco mais (opcional)")
    
    submit = st.form_submit_button("Enviar com Propósito")
    
    if submit:
        if nome:
            # Seu número já configurado corretamente
            numero_whatsapp = "5512996069640" 
            
            texto = f"Olá! Meu nome é {nome}. Vi o seu site e gostaria de falar sobre {ajuda}. {mensagem_extra}"
            texto_url = urllib.parse.quote(texto)
            link_wa = f"https://wa.me/{numero_whatsapp}?text={texto_url}"
            
            st.markdown(f'''
                <a href="{link_wa}" target="_blank" style="text-decoration: none;">
                    <div style="background-color: #25D366; color: white; border-radius: 20px; width: 100%; height: 3em; font-weight: bold; display: flex; align-items: center; justify-content: center; text-align: center; cursor: pointer;">
                        ✅ CLIQUE AQUI PARA CONFIRMAR NO WHATSAPP
                    </div>
                </a>
            ''', unsafe_allow_html=True)
            st.success("Quase lá! Clique no botão verde acima para abrir o seu WhatsApp.")
        else:
            st.error("Por favor, preencha o seu nome.")

st.caption("© 2026 - Governe Sua História | Design Rosa & Black")
