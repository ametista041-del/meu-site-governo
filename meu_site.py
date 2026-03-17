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
   
   
   ,# 1. CÁLCULO AUTOMÁTICO (Baseado no que o usuário preencheu)
    media_roda = (n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12) / 12
    nota_conexao = n10

    st.markdown("---")
    st.markdown(f"<h1 style='text-align: center; color: #D4AF37;'>💎 Seu Diagnóstico Exclusivo</h1>", unsafe_allow_html=True)

    # --- FEEDBACK INDIVIDUALIZADO: RODA DA VIDA ---
    st.subheader("🎡 Parte 1: Seu Mapa de Autogoverno")
    
    # O gráfico já reflete os dados exatos do teste
    df_radar = pd.DataFrame(dict(
        r=[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12],
        theta=['Saúde', 'Intelectual', 'Emocional', 'Espiritual', 'Finanças', 'Profissional', 'Social', 'Lazer', 'Família', 'Amor', 'Amizades', 'Felicidade']
    ))
    fig1 = px.line_polar(df_radar, r='r', theta='theta', line_close=True)
    fig1.update_traces(fill='toself', fillcolor='rgba(212, 175, 55, 0.4)', line=dict(color="#D4AF37", width=4))
    fig1.update_layout(polar=dict(bgcolor="rgba(0,0,0,0)", radialaxis=dict(visible=True, range=[0, 10])), paper_bgcolor="rgba(0,0,0,0)", showlegend=False)
    st.plotly_chart(fig1, use_container_width=True)

    # Lógica de Feedback da Roda (Cada um recebe um texto diferente)
    if media_roda <= 4:
        st.error(f"**Análise de Perfil: Sobrevivente.** Sua média de {media_roda:.1f} indica que você está perdendo o governo sobre sua rotina. As áreas com notas baixas estão drenando sua energia vital. É impossível transbordar com uma estrutura tão fragilizada.")
    elif 4 < media_roda <= 7:
        st.warning(f"**Análise de Perfil: Gestor em Equilíbrio.** Com média de {media_roda:.1f}, você já governa algumas áreas, mas possui 'pontos cegos'. Sua roda tem oscilações que geram cansaço desnecessário. O foco agora é estabilizar os pilares mais fracos.")
    else:
        st.success(f"**Análise de Perfil: Governante Ativo.** Parabéns! Sua média de {media_roda:.1f} é excelente. Você tem domínio sobre sua história e está em plena fase de transbordo.")

    st.write("---")

    # --- FEEDBACK INDIVIDUALIZADO: IDENTIDADE DE CONEXÃO ---
    st.subheader("🎯 Parte 2: Sua Identidade de Conexão")
    
    # Gráfico que muda de cor conforme a nota
    fig2 = px.bar(x=[nota_conexao], y=["Conexão"], orientation='h', range_x=[0,10], color=[nota_conexao], color_continuous_scale='Sunset')
    fig2.update_layout(height=150, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", coloraxis_showscale=False, yaxis=dict(visible=False))
    st.plotly_chart(fig2, use_container_width=True)

    # Lógica de Feedback de Conexão (Baseado no Pilar n10)
    if nota_conexao <= 4:
        st.info("**Sua Linguagem: Tempo de Qualidade.**\n\nSua alma pede presença. O diagnóstico mostra que para você governar, você precisa parar de 'fazer' e começar a 'ser'. Sem tempo de qualidade, sua conexão com o propósito se perde.")
    elif 5 <= nota_conexao <= 7:
        st.info("**Sua Linguagem: Atos de Serviço.**\n\nSua forma de governar é através do cuidado prático. O teste revela que você se sente amado e no comando quando vê resultados tangíveis e ajuda mútua.")
    else:
        st.info("**Sua Linguagem: Palavras de Afirmação.**\n\nO diagnóstico confirma: sua palavra tem poder. O incentivo e o reconhecimento são o combustível para o seu autogoverno. Se você não usa sua voz, seu comando enfraquece.")

    # --- VEREDITO FINAL (SOMA TOTAL) ---
    st.write("---")
    resultado_final = (media_roda + nota_conexao) / 2
    st.markdown(f"<h3 style='text-align: center;'>Índice Geral de Comando: {resultado_final:.1f}</h3>", unsafe_allow_html=True)
    
    if resultado_final < 6:
        st.error("🛑 **AÇÃO IMEDIATA:** O governo da sua história precisa de uma intervenção nas áreas de base. Não tente transbordar antes de consertar os vazamentos da sua roda.")
    else:
        st.success("👑 **STATUS:** Você está no comando. Continue governando com clareza e usando sua identidade de conexão para impactar quem está ao seu redor.")