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
        ser apenas 'filha'. Este é o coração do meu futuro livro e da minha mentoria.
        """)
    #with col4: st.image("foto.jpg", use_container_width=True)

    st.markdown("---")
    
    # Ato 3: Reconstrução em Portugal (Foto 5)
    col5, col6 = st.columns([1, 2])
    #with col5: st.image("foto5.jpg", use_container_width=True)
    with col6: 
        st.subheader("O Transbordo: Portugal e o Novo Início")
        st.write("""
        Hoje, vivendo em Portugal e casada com o Bruno de Noronha, vivo o transbordo da minha reconstrução. 
        A prova de que o governo da alma gera um destino novo. Sou mentora de mulheres que decidiram, 
        assim como eu, que o capítulo passado não define o final da história.
        """)
        st.markdown(f'<a href="https://wa.me/5565992348575" target="_blank"><button style="background-color: #25D366; color: white; border: none; padding: 10px 20px; border-radius: 10px; cursor: pointer; font-weight: bold;">Fale Comigo no WhatsApp</button></a>', unsafe_allow_html=True)

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
    if btn_final:
        st.markdown("<div class='caixa-bio'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #D4AF37;'>Seu Veredito de Governança</h3>", unsafe_allow_html=True)
        
        media = (n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12)/12
        st.write(f"Sua média geral de equilíbrio: **{media:.1f} / 10**")
        
        # Gráfico Polar/Radar
        df = pd.DataFrame(dict(
            r=[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12],
            theta=['Saúde','Intelectual','Emocional','Espiritual','Finanças','Profissional','Social','Lazer','Família','Amor','Amizades','Felicidade']))
        fig = px.line_polar(df, r='r', theta='theta', line_close=True)
        fig.update_traces(fill='toself', fillcolor='rgba(212, 175, 55, 0.5)', line_color="#D4AF37", line_width=3)
        fig.update_layout(polar=dict(bgcolor="#1E2117"), showlegend=False)
        st.plotly_chart(fig)
        
        st.write("---")
        st.subheader("Resumo das Linguagens")
        st.write(f"Sua maior conexão vem de: **Atos de Serviço e Tempo de Qualidade** (Exemplo)")
        
        if media < 6:
            st.info("💡 Insight: Sua governança precisa de um alicerce mais forte. Comece organizando o pilar espiritual e emocional.")
        else:
            st.success("💡 Insight: Você tem um bom nível de governo pessoal. O próximo passo é o transbordo na vida de outros.")
        st.markdown("</div>", unsafe_allow_html=True)
        

