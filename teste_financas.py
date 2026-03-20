import streamlit as st
import pandas as pd
import pdfplumber
import re
from datetime import date

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Gestão Financeira", layout="wide", page_icon="💰")

# 2. ESTADO DO APLICATIVO (Banco de dados temporário)
if 'transacoes' not in st.session_state:
    st.session_state.transacoes = []

# 3. FUNÇÃO PARA EXTRAIR VALOR DO TEXTO DO PDF
def extrair_valor_reais(texto):
    padrao_valor = r"(?:R\$\s?)?(\d{1,3}(?:\.\d{3})*,\d{2})"
    resultado = re.search(padrao_valor, texto)
    if resultado:
        valor_str = resultado.group(1)
        return float(valor_str.replace('.', '').replace(',', '.'))
    return 0.0

# --- BARRA LATERAL ---
st.sidebar.header("⚙️ Entradas de Dados")

# Aba de Lançamento Manual
with st.sidebar.expander("➕ Lançamento Manual", expanded=True):
    with st.form("form_manual"):
        tipo_m = st.selectbox("Tipo", ["Saída (Gasto)", "Entrada (Ganho)"])
        desc_m = st.text_input("Descrição")
        valor_m = st.number_input("Valor (R$)", min_value=0.0, step=1.0, format="%.2f")
        data_m = st.date_input("Data", value=date.today())
        btn_m = st.form_submit_button("Adicionar Manual")
        
        if btn_m and desc_m and valor_m > 0:
            v_final = -valor_m if tipo_m == "Saída (Gasto)" else valor_m
            st.session_state.transacoes.append({
                "Data": data_m, "Descrição": desc_m, "Tipo": tipo_m, "Valor (R$)": v_final
            })
            st.sidebar.success("Adicionado!")

# Aba de Upload de PDF
with st.sidebar.expander("📄 Importar PDF (Extratos)"):
    arquivo_pdf = st.file_uploader("Suba o PDF do banco", type=["pdf"])
    if arquivo_pdf:
        if st.button("Processar PDF"):
            with pdfplumber.open(arquivo_pdf) as pdf:
                for pagina in pdf.pages:
                    texto = pagina.extract_text()
                    if texto:
                        for linha in texto.split('\n'):
                            v = extrair_valor_reais(linha)
                            if v > 0:
                                # Lógica simples: se tem "recebido" é entrada, senão saída
                                tipo_p = "Entrada (Ganho)" if "recebido" in linha.lower() or "pix" in linha.lower() else "Saída (Gasto)"
                                v_p = v if tipo_p == "Entrada (Ganho)" else -v
                                st.session_state.transacoes.append({
                                    "Data": date.today(), "Descrição": linha.strip()[:50], "Tipo": tipo_p, "Valor (R$)": v_p
                                })
            st.sidebar.success("PDF Processado!")

# --- ÁREA PRINCIPAL ---
st.title("📊 Painel de Controle de Gastos")

if st.session_state.transacoes:
    df = pd.DataFrame(st.session_state.transacoes)
    
    # Cálculos para os Cards
    total_in = df[df['Valor (R$)'] > 0]['Valor (R$)'].sum()
    total_out = abs(df[df['Valor (R$)'] < 0]['Valor (R$)'].sum())
    saldo = total_in - total_out

    # Exibição dos Indicadores
    c1, c2, c3 = st.columns(3)
    c1.metric("📈 Entradas", f"R$ {total_in:,.2f}")
    c2.metric("📉 Saídas", f"R$ {total_out:,.2f}")
    c3.metric("⚖️ Saldo Atual", f"R$ {saldo:,.2f}")

    st.divider()

    # Tabela e Gráfico
    col_t, col_g = st.columns([1.5, 1])
    
    with col_t:
        st.subheader("📋 Movimentações")
        st.dataframe(df, use_container_width=True)
        if st.button("🗑️ Limpar Tudo"):
            st.session_state.transacoes = []
            st.rerun()

    with col_g:
        st.subheader("🥧 Distribuição")
        df_pizza = pd.DataFrame({
            "Tipo": ["Entradas", "Saídas"],
            "Valor": [total_in, total_out]
        })
        st.vega_lite_chart(df_pizza, {
            'mark': {'type': 'arc', 'innerRadius': 50},
            'encoding': {
                'theta': {'field': 'Valor', 'type': 'quantitative'},
                'color': {'field': 'Tipo', 'type': 'nominal', 'scale': {'range': ['#2ecc71', '#e74c3c']}},
            }
        }, use_container_width=True)
else:
    st.info("👋 O sistema está pronto! Use a barra lateral para lançar seus gastos ou subir um PDF.")