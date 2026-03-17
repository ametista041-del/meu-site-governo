import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURAÇÃO DE PÁGINA E ESTILO VISUAL (VERDE MILITAR & DOURADO)
st.set_page_config(page_title="Adriana Noronha | Governe sua História", layout="wide")

st.markdown("""
    <style>
    /* Fundo Verde Militar */
    .stApp { background-color: #2F3526; } 
    
    /* Fontes e Cores Gerais */
    p, li, span, label, h1, h2, h3, h4 { color: #F5F5F5 !important; font-family: 'Georgia', serif; }
    
    /* Caixas de Texto Estilizadas */
    .caixa-bio {
        background-color: #3B4232; padding: 35px; border-radius: 20px;
        border-left: 10px solid #D4AF37; margin-bottom: 30px;
        box-shadow: 6px 6px 15px rgba(0,0,0,0.4);
    }
    
    /* Estilo dos Títulos de Seção */
    .titulo-dourado { color: #D4AF37 !important; font-weight: bold; border-bottom: 1px solid #D4AF37; padding-bottom: 10px; }
    
    /* Abas Personalizadas */
    .stTabs [aria-selected="true"] { color: #D4AF37 !important; border-bottom-color: #D4AF37 !important; font-size: 20px; }
    
    /* Botão Principal Dourado */
    .stButton>button { 
        background-color: #D4AF37; color: #2F3526; font-weight: bold; 
        border-radius: 12px; width: 100%; border: none; height: 55px; 
        transition: 0.3s; font-size: 18px;
    }
    .stButton>button:hover { background-color: #B8962E; color: #FFFFFF; }
    
    /* Imagens com borda sutil */
    img { border-radius: 15px; border: 1px solid #4A5240; }
    </style>
""", unsafe_allow_html=True)

# 2. BARRA LATERAL (Persona Digital Elsa)
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>Bem-vinda</h2>", unsafe_allow_html=True)
    st.video("persona.mp4", autoplay=True, muted=True)
    st.markdown("---")
    st.write("Sua jornada de autoconhecimento começa aqui. Governe cada área da sua vida com sabedoria e fé.")
    st.caption("Site Oficial | Adriana Noronha")

# 3. CABEÇALHO PRINCIPAL
st.markdown("✨ Adriana De Noronha", unsafe_allow_html=True)
st.markdown("<div class='caixa-bio'><i style='color: #D4AF37;'>\"Deus não me chamou para ser um cargo: Ele chamou-me de 'filhinha'.\"</i></div>", unsafe_allow_html=True)  

# 4. SISTEMA DE ABAS
aba1, aba2 = st.tabs(["🌱 Minha Jornada & Reconstrução", "🎡 Diagnóstico de Autoconhecimento"])

# --- ABA 1: NARRATIVA ---
with aba1:
    # Ato 1: A Lógica da Líder (Foto 4)
    col1, col2 = st.columns([1, 2])
    with col1: st.image("foto4.jpg", use_container_width=True)
    with col2: 
        st.subheader("A Estrutura por trás da Líder")
        st.write("""
        Com mais de 25 anos de experiência em gestão e formação em áreas técnicas e de RH, 
        aprendi que processos precisam de ordem, mas pessoas precisam de governo. 
        Minha trajetória é marcada pela busca constante pela excelência e pela liderança que transforma.
        """)
    
    st.markdown("---")
    
    # Ato 2: O Deserto (foto.jpg)
    col3, col4 = st.columns([2, 1])
    with col3: 
        st.subheader("O Divórcio que me Aproximou de Deus")
        st.write("""
        Aos 45 anos, após duas décadas de casamento, vi minha estrutura ruir. No silêncio do deserto e da rejeição, 
        entendi que a maior governança é sobre o próprio coração. Foi onde deixei cargos e títulos para 
        ser apenas 'filha'. me senti amada e acolhida por Deus. E pronta pra começar a reconstrução da minha história, agora com um novo propósito: ajudar outras mulheres a governarem suas vidas e se reconectarem com o amor divino.
        """)
    with col4: st.image("foto.Jpg", use_container_width=True)

    st.markdown("---")
    
    # Ato 3: Reconstrução em Portugal (Foto 5)
    col5, col6 = st.columns([1, 2])
    with col5: st.image("foto5.jpg", use_container_width=True)
    with col6: 
        st.subheader("O Transbordo: Portugal e o Novo Início")
        st.write("""
        Hoje, vivendo em Portugal e casada com o Bruno de Noronha, vivo o transbordo da minha reconstrução. 
        A prova de que o governo da alma gera um destino novo. Sou mentora de mulheres que decidiram, 
        assim como eu, que o capítulo passado não define o final da história.
        """)
        st.markdown(f'<a href="https://wa.me/5512996069640" target="_blank"><button style="background-color: #25D366; color: white; border: none; padding: 10px 20px; border-radius: 10px; cursor: pointer; font-weight: bold;">Fale Comigo no WhatsApp</button></a>', unsafe_allow_html=True)

# --- ABA 2: FERRAMENTAS DE GOVERNANÇA ---
with aba2:
    st.markdown("<h2 class='titulo-dourado'>Painel de Diagnóstico Pessoal</h2>", unsafe_allow_html=True)
    st.write("Avalie-se com sinceridade. O resultado aparecerá logo após você clicar no botão ao final.")
    
    with st.form("diagnostico_governo"):
        # Roda da Vida
        st.subheader("1. Roda da Vida (Equilíbrio dos 12 Pilares)")
        c1, c2, c3 = st.columns(3)
        with c1:
            n1 = st.slider("Saúde", 0, 10, 5); n2 = st.slider("Intelectual", 0, 10, 5)
            n3 = st.slider("Emocional", 0, 10, 5); n4 = st.slider("Espiritual", 0, 10, 5)
        with c2:
            n5 = st.slider("Financeiro", 0, 10, 5); n6 = st.slider("Profissional", 0, 10, 5)
            n7 = st.slider("Social", 0, 10, 5); n8 = st.slider("Lazer", 0, 10, 5)
        with c3:
            n9 = st.slider("Família", 0, 10, 5); n10 = st.slider("Amor", 0, 10, 5)
            n11 = st.slider("Amizades", 0, 10, 5); n12 = st.slider("Felicidade", 0, 10, 5)
        
        st.markdown("---")
        
        # Linguagens do Amor
        st.subheader("2. Linguagens do Amor (Conexão e Relacionamentos)")
        st.write("O quanto cada linguagem é importante para você se sentir amada?")
        l1 = st.select_slider("Palavras de Afirmação", options=["Baixo", "Médio", "Alto"], value="Médio")
        l2 = st.select_slider("Tempo de Qualidade", options=["Baixo", "Médio", "Alto"], value="Médio")
        l3 = st.select_slider("Presentes", options=["Baixo", "Médio", "Alto"], value="Médio")
        l4 = st.select_slider("Atos de Serviço", options=["Baixo", "Médio", "Alto"], value="Médio")
        l5 = st.select_slider("Toque Físico", options=["Baixo", "Médio", "Alto"], value="Médio")
        
        btn_final = st.form_submit_button("GERAR MEU DIAGNÓSTICO AGORA")

    # RESULTADO (SÓ APARECE APÓS O CLICK)
   
   # === PROCESSAMENTO PREMIUM DO RESULTADO ===
    media_governanca = (n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12) / 12
    indice_total = (media_governanca + n10) / 2 # A média de tudo

    st.markdown("---")
    st.markdown(f"<h1 style='text-align: center; color: #D4AF37;'>💎 Seu Diagnóstico Governe sua História</h1>", unsafe_allow_html=True)
    st.write(f"<h3 style='text-align: center;'>Pontuação Geral de Comando: **{indice_total:.1f}** / 10</h3>", unsafe_allow_html=True)
    st.write("##") # Espaçamento

    # --- FERRAMENTA 1: MAPA DE AUTOGOVERNO (Design Premium) ---
    st.subheader("🎡 1. Mapa de Autogoverno (Equilíbrio)")
    
    df_radar = pd.DataFrame(dict(
        r=[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12],
        theta=['Saúde', 'Intelectual', 'Emocional', 'Espiritual', 'Finanças', 'Profissional', 'Social', 'Lazer', 'Família', 'Amor', 'Amizades', 'Felicidade']
    ))
    
    fig_radar = px.line_polar(df_radar, r='r', theta='theta', line_close=True)
    
    # === AQUI ESTÁ O AJUSTE VISUAL PREMIUM ===
    fig_radar.update_traces(
        fill='toself', 
        fillcolor='rgba(212, 175, 55, 0.6)', # Dourado suave preenchendo
        line=dict(color="#D4AF37", width=6) # Linha dourada grossa
    )
    fig_radar.update_layout(
        polar=dict(
            bgcolor="rgba(0,0,0,0)", # Fundo transparente para casar com o site
            radialaxis=dict(visible=True, range=[0, 10], gridcolor="#888", linecolor="#444"),
            angularaxis=dict(gridcolor="#444", tickfont=dict(size=11))
        ),
        paper_bgcolor="rgba(0,0,0,0)", # Fundo do papel transparente
        showlegend=False,
        margin=dict(l=80, r=80, t=40, b=40)
    )
    st.plotly_chart(fig_radar, use_container_width=True)

    st.write("---")

    # --- FERRAMENTA 2: FORÇA DE CONEXÃO (Design Premium) ---
    st.subheader("🎯 2. Sua Força de Conexão")
    
    # Gráfico de Barras Premium
    df_bar = pd.DataFrame({'Área': ['Sua Nota'], 'Valor': [n10]})
    fig_bar = px.bar(df_bar, x='Valor', y='Área', orientation='h', range_x=[0,10])
    
    # === AJUSTE VISUAL DA BARRA ===
    fig_bar.update_traces(
        marker_color="#D4AF37", # Dourado Conexão
        marker_line=dict(color="#FFF", width=1)
    )
    fig_bar.update_layout(
        height=180,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=20, b=20),
        xaxis=dict(gridcolor="#333", visible=True),
        yaxis=dict(visible=False) # Esconde o nome "Sua Nota"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    # Texto Explicativo da Conexão
    if n10 <= 4:
        st.info("✨ **Tempo de Qualidade.** Para governar sua história, você precisa, primeiro, estar presente na sua própria vida.")
    elif 5 <= n10 <= 7:
        st.info("✨ **Atos de Serviço.** O amor se manifesta no cuidado prático. Governe através do servir.")
    else:
        st.info("✨ **Palavras de Afirmação.** O incentivo é o seu combustível de governo. Use sua voz para transbordar.")

    st.write("---")

    # === VEREDITO FINAL (Inteligência Premium) ===
    st.header("💡 Veredito de Governança")
    
    # Análise de Perfil baseada no desequilíbrio (exemplo)
    tem_nota_baixa = n1<5 or n3<5 or n9<5 or n10<5
    
    with st.expander("🔍 Ver Análise Detalhada (Aperte para ler)", expanded=tem_nota_baixa):
        st.markdown(f"### O Índice de **{indice_total:.1f}** revela o seguinte cenário:")
        
        # Etapa 1: O Perfil
        if media_governanca < 6 and n10 > 7:
            st.write("🩸 **Perfil Gestor Esgotado:** Você tem uma força de conexão alta (Palavras de Afirmação), mas sua Roda da Vida está travando. Você está transbordando para os outros o que está faltando em você.")
        elif media_governanca > 7 and n10 < 5:
            st.write("🧱 **Perfil Piloto Automático:** Sua Roda da Vida está equilibrada, mas sua Conexão (pilar Amor) é baixa. Você está performando, mas não está se conectando profundamente. Falta o transbordo da alma.")
        else:
            st.write("Governar não é equilibrar pratos, é direcionar energia. Seus gráficos mostram onde sua energia está vindo e onde ela está vazando.")

        # Etapa 2: O Impacto no Transbordo
        st.markdown("### O Impacto no Transbordo:")
        if indice_total < 6:
            st.warning("⚠️ **Bloqueio de Fluidez:** Com este nível de governança, você é um reservatório furado. O que você ganha com o amor se perde no desequilíbrio das outras áreas. O transbordo é travado pela falta de integridade estrutural na sua vida.")
        else:
            st.success("✅ **Fluidez Ativa:** Parabéns! Você já é uma fonte. Seu desafio agora é não apenas governar, mas garantir que a fonte nunca seque através do autogerenciamento constante.")

        # Etapa 3: O Plano de Ação
        st.markdown("### 🛠 Três Passos para Retomar o Comando:")
        if tem_nota_baixa:
            st.write(f"1.  **Eliminação Imediata:** A área com nota **{(min(n1,n3,n9,n10)):.1f}** está roubando seu governo. Liste três ações para resolver isso amanhã.\n2.  **Uso da Força:** Sua maior nota é na Conexão ({n10:.1f}). Use essa força para te dar energia para lidar com o problema.\n3.  **Monitoramento Diário:** Não espere o caos. Baixe as outras áreas se necessário para levantar a principal. O comando é dinâmico.")
        else:
            st.write("1.  **Transbordo Estratégico:** Qual área você pode delegar ou simplificar para focar ainda mais no que te dá mais energia?\n2.  **Elevação da Barra:** Onde você pode tirar 10 e levar para 11?\n3.  **Ensino:** Seu governo é um exemplo. Quem você pode mentorear nessa fase?")

    st.caption("Governe sua História © 2026 | Adriana de Noronha")