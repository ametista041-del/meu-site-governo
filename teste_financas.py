import streamlit as st
import pandas as pd
import pdfplumber
import re
import pytesseract
import os
from PIL import Image
from datetime import date

# --- 1. MOTOR DE VISÃO (INTELIGÊNCIA HÍBRIDA) ---
# Detecta se está no seu computador ou no servidor da internet
if os.path.exists(r'C:\Program Files\Tesseract-OCR\tesseract.exe'):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# --- 2. CONFIGURAÇÃO VISUAL (ESTILO NORONHA) ---
st.set_page_config(page_title="Gestão Financeira - Noronha", layout="wide", page_icon="💰")

COR_OURO = "#D4AF37"
COR_VERDE_MILITAR = "#4B5320"

st.markdown(f"""
    <style>
    .stApp {{ background-color: #F8F9FA; }}
    h1, h2 {{ color: {COR_VERDE_MILITAR}; text-align: center; }}
    .stMetric {{ background-color: #ffffff; padding: 15px; border-radius: 10px; border-left: 5px solid {COR_OURO}; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }}
    </style>
    """, unsafe_allow_html=True)

if 'transacoes' not in st.session_state:
    st.session_state.transacoes = []

# --- 3. LÓGICA DE LIMPEZA (FILTRO DE PRECISÃO) ---

def extrair_valor_limpo(texto):
    """Identifica valores reais e ignora lixo de índices e saldos bancários"""
    texto_up = texto.upper()
    
    # LISTA NEGRA: Palavras que o código ignora para o saldo ser 100% REAL
    bloqueados = [
        "EURO", "DOLAR", "DÓLAR", "IBOVESPA", "SALARIO", "SALÁRIO", 
        "LIMITE", "RESUMO", "TOTAL DA FATURA", "TOTAL A PAGAR", 
        "SALDO ANTERIOR", "PAGAMENTO MÍNIMO", "ENCARGOS", "INDICADORES", 
        "VARIAÇÃO", "SALDO EM", "SALDO DE CONTA", "SALDO DISPONÍVEL"
    ]
    
    if any(b in texto_up for b in bloqueados):
        return 0.0

    # Busca valores financeiros (Ex: 1.234,56)
    padrao = r"(?:R\$?\s?)?(\d{1,3}(?:\.\d{3})*,\d{2})"
    resultado = re.search(padrao, texto)
    if resultado:
        val_str = resultado.group(1)
        return float(val_str.replace('.', '').replace(',', '.'))
    return 0.0

def processar_sequencia_texto(texto_bruto, origem):
    """Filtra apenas transações reais que possuem uma data na linha"""
    padrao_data = r"(\d{2}/\d{2}|\d{2}\s[A-Z]{3})"
    
    linhas = texto_bruto.split('\n')
    for linha in linhas:
        valor = extrair_valor_limpo(linha)
        
        # Só aceita se tiver VALOR e uma DATA na mesma linha (evita títulos e lixo)
        if valor > 0.01 and re.search(padrao_data, linha.upper()):
            ganhos = ["PIX RECEBIDO", "DEPOSITO", "RECEBIDO", "ESTORNO", "CRÉDITO", "TRANSFERÊNCIA RECEBIDA"]
            eh_entrada = any(g in linha.upper() for g in ganhos)
            
            tipo = "Entrada (Ganho)" if eh_entrada else "Saída (Gasto)"
            v_final = valor if eh_entrada else -valor
            
            st.session_state.transacoes.append({
                "Data": date.today(),
                "Descrição": f"[{origem}] {linha.strip()[:50]}",
                "Tipo": tipo,
                "Valor (R$)": v_final
            })

# --- 4. INTERFACE DO USUÁRIO ---

st.title("📊 Painel Financeiro - Governe sua História")

st.sidebar.header("📂 Importar Comprovantes")
with st.sidebar.expander("📸 Enviar PDF ou Print"):
    arquivo = st.file_uploader("Arraste aqui", type=["pdf", "png", "jpg", "jpeg"])
    if arquivo and st.button("Processar Agora"):
        if arquivo.type == "application/pdf":
            with pdfplumber.open(arquivo) as pdf:
                texto_total = ""
                for p in pdf.pages:
                    texto_total += p.extract_text() or ""
                processar_sequencia_texto(texto_total, "PDF")
        else:
            img = Image.open(arquivo)
            try:
                texto_img = pytesseract.image_to_string(img, lang='por+spa')
                processar_sequencia_texto(texto_img, "PRINT")
            except Exception:
                st.error("Erro no motor de visão. Tente subir um PDF.")
        st.sidebar.success("Processado!")

# Exibição dos Resultados
if st.session_state.transacoes:
    df = pd.DataFrame(st.session_state.transacoes)
    
    entradas = df[df['Valor (R$)'] > 0]['Valor (R$)'].sum()
    saidas = abs(df[df['Valor (R$)'] < 0]['Valor (R$)'].sum())
    saldo = entradas - saidas

    c1, c2, c3 = st.columns(3)
    c1.metric("Ganhos (Ouro)", f"R$ {entradas:,.2f}")
    c2.metric("Gastos (Militar)", f"R$ {saidas:,.2f}")
    c3.metric("Saldo Real", f"R$ {saldo:,.2f}")

    st.divider()

    col_t, col_g = st.columns([2, 1])
    
    with col_t:
        st.subheader("📋 Movimentações Reais")
        st.dataframe(df, use_container_width=True)
        if st.button("🗑️ Limpar Tudo"):
            st.session_state.transacoes = []
            st.rerun()

    with col_g:
        st.subheader("🍩 Distribuição")
        df_pizza = pd.DataFrame({"Tipo": ["Ganhos", "Gastos"], "Valor": [entradas, saidas]})
        st.vega_lite_chart(df_pizza, {
            'mark': {'type': 'arc', 'innerRadius': 50},
            'encoding': {
                'theta': {'field': 'Valor', 'type': 'quantitative'},
                'color': {
                    'field': 'Tipo', 'type': 'nominal', 
                    'scale': {'range': [COR_OURO, COR_VERDE_MILITAR]}
                }
            }
        }, use_container_width=True)
else:
    st.info("Olá, Adriana Noronha! Suba seus documentos na lateral para começar.")