import streamlit as st
import pandas as pd
import pdfplumber
import re
from datetime import date

# 1. CONFIGURAÇÃO DA PÁGINA (Identidade Adriana Noronha)
st.set_page_config(page_title="Gestão Financeira - Noronha", layout="wide", page_icon="💰")

# Cores da Marca
COR_OURO = "#D4AF37"
COR_VERDE_MILITAR = "#4B5320"

st.markdown(f"""
    <style>
    .stApp {{ background-color: #FAFAFA; }}
    h1 {{ color: {COR_VERDE_MILITAR}; }}
    </style>
    """, unsafe_allow_html=True)

if 'transacoes' not in st.session_state:
    st.session_state.transacoes = []

# 2. FUNÇÃO PARA EXTRAIR VALOR (Melhorada)
def extrair_valor_reais(texto):
    # Ignorar índices econômicos que confundem o cálculo
    termos_bloqueados = ["IBOVESPA", "IGPM", "INPC", "IPCA", "CDI", "SELIC"]
    if any(termo in texto.upper() for termo in termos_bloqueados):
        return 0.0
    
    padrao_valor = r"(?:R\$?\s?)?(\d{1,3}(?:\.\d{3})*,\d{2})"
    resultado = re.search(padrao_valor, texto)
    if resultado:
        valor_str = resultado.group(1)
        valor_limpo = float(valor_str.replace('.', '').replace(',', '.'))
        return valor_limpo if valor_limpo > 1.0 else 0.0 # Ignora valores irrelevantes
    return 0.0

# 3. BARRA LATERAL
st.sidebar.header("📂 Entrada de Dados")

with st.sidebar.expander("📝 Lançamento Manual"):
    with st.form("form_manual"):
        tipo_m = st.selectbox("Tipo", ["Saída (Gasto)", "Entrada (Ganho)"])
        desc_m = st.text_input("Descrição")
        valor_m = st.number_input("Valor (R$)", min_value=0.0, step=1.0)
        btn_m = st.form_submit_button("Adicionar")
        
        if btn_m and desc_m and valor_m > 0:
            v_final = -valor_m if tipo_m == "Saída (Gasto)" else valor_m
            st.session_state.transacoes.append({
                "Data": date.today(), "Descrição": desc_m, "Tipo": tipo_m, "Valor (R$)": v_final
            })
            st.sidebar.success("Adicionado!")

with st.sidebar.expander("📄 Importar PDF"):
    arquivo_pdf = st.file_uploader("Suba o extrato do banco", type=["pdf"])
    if arquivo_pdf and st.button("Processar PDF"):
        with pdfplumber.open(arquivo_pdf) as pdf:
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if texto:
                    for linha in texto.split('\n'):
                        v = extrair_valor_reais(linha)
                        if v > 0:
                            # Lógica: se tiver "PIX" ou "RECEBIDO" é entrada
                            tipo_p = "Entrada (Ganho)" if any(x in linha.lower() for x in ["pix", "recebido", "deposito"]) else "Saída (Gasto)"
                            v_p = v if tipo_p == "Entrada (Ganho)" else -v
                            st.session_state.transacoes.append({
                                "Data": date.today(), "Descrição": linha.strip()[:50], "Tipo": tipo_p, "Valor (R$)": v_p
                            })
        st.sidebar.success("PDF Processado com Filtros!")

# 4. ÁREA PRINCIPAL
st.title("📊 Painel de Controle de Gastos")

if st.session_state.transacoes:
    df = pd.DataFrame(st.session_state.transacoes)
    
    t_in = df[df['Valor (R$)'] > 0]['Valor (R$)'].sum()
    t_out = abs(df[df['Valor (R$)'] < 0]['Valor (R$)'].sum())
    saldo = t_in - t_out

    c1, c2, c3 = st.columns(3)
    c1.metric("Entradas (Ouro)", f"R$ {t_in:,.2f}")
    c2.metric("Saídas (Militar)", f"R$ {t_out:,.2f}")
    c3.metric("Saldo Atual", f"R$ {saldo:,.2f}")

    col_t, col_g = st.columns([2, 1])
    
    with col_t:
        st.subheader("📋 Movimentações")
        st.dataframe(df, use_container_width=True)
        if st.button("🗑️ Limpar Tudo"):
            st.session_state.transacoes = []
            st.rerun()

    with col_g:
        st.subheader("🍩 Distribuição")
        df_pizza = pd.DataFrame({
            "Tipo": ["Entradas", "Saídas"],
            "Valor": [t_in, t_out]
        })
        st.vega_lite_chart(df_pizza, {
            'mark': {'type': 'arc', 'innerRadius': 50},
            'encoding': {
                'theta': {'field': 'Valor', 'type': 'quantitative'},
                'color': {'field': 'Tipo', 'type': 'nominal', 'scale': {'range': [COR_OURO, COR_VERDE_MILITAR]}}
            }
        }, use_container_width=True)
else:
    st.info("O sistema está pronto! Use a barra lateral para subir um PDF.")