import streamlit as st
import pandas as pd
import pdfplumber
import re
import pytesseract
from PIL import Image
from datetime import date

# --- CONFIGURAÇÃO DO TESSERACT (O MOTOR DE VISÃO NO WINDOWS) ---
# Esta linha liga o Python ao programa que você instalou agora
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# --- 1. CONFIGURAÇÃO DA PÁGINA (Estilo Noronha) ---
st.set_page_config(page_title="Gestão Financeira - Noronha", layout="wide", page_icon="💰")

# Cores Oficiais
COR_OURO = "#D4AF37"
COR_VERDE_MILITAR = "#4B5320"

st.markdown(f"""
    <style>
    .stApp {{ background-color: #F8F9FA; }}
    h1, h2, h3 {{ color: {COR_VERDE_MILITAR}; }}
    .stMetric {{ background-color: #ffffff; padding: 15px; border-radius: 10px; border-left: 5px solid {COR_OURO}; }}
    </style>
    """, unsafe_allow_html=True)

if 'transacoes' not in st.session_state:
    st.session_state.transacoes = []

# --- 2. FUNÇÕES DE INTELIGÊNCIA ---

def limpar_valor(texto):
    """Extrai apenas o número financeiro de uma linha de texto"""
    texto_up = texto.upper()
    
    # FILTRO: Ignora indicadores que não são gastos/ganhos da Adriana
    bloqueados = ["EURO", "DOLAR", "DÓLAR", "IBOVESPA", "IGPM", "INPC", "IPCA", "SALÁRIO MÍNIMO", "TAXA", "RESUMO"]
    if any(b in texto_up for b in bloqueados):
        return 0.0

    # Busca o formato de moeda R$ ou apenas números com vírgula
    padrao = r"(?:R\$?\s?)?(\d{1,3}(?:\.\d{3})*,\d{2})"
    resultado = re.search(padrao, texto)
    if resultado:
        val_str = resultado.group(1)
        return float(val_str.replace('.', '').replace(',', '.'))
    return 0.0

def processar_linhas_texto(texto_bruto, origem):
    """Transforma blocos de texto em registros na tabela"""
    confirmadores = ["PIX", "COMPRA", "DEBITO", "DÉBITO", "CREDITO", "CRÉDITO", "PAGAMENTO", "RECEBIDO", "TRANSFERÊNCIA"]
    
    for linha in texto_bruto.split('\n'):
        valor = limpar_valor(linha)
        if valor > 0.50: # Ignora centavos irrelevantes
            # Define se é entrada ou saída baseado em palavras-chave
            eh_entrada = any(palavra in linha.upper() for palavra in ["PIX RECEBIDO", "DEPOSITO", "CRÉDITO", "RECEBIDO"])
            tipo = "Entrada (Ganho)" if eh_entrada else "Saída (Gasto)"
            valor_final = valor if eh_entrada else -valor
            
            st.session_state.transacoes.append({
                "Data": date.today(),
                "Descrição": f"[{origem}] {linha.strip()[:40]}...",
                "Tipo": tipo,
                "Valor (R$)": valor_final
            })

# --- 3. INTERFACE LATERAL ---
st.sidebar.header("📂 Importar Movimentações")

with st.sidebar.expander("📝 Lançamento Manual"):
    with st.form("manual_form"):
        t = st.selectbox("Tipo", ["Saída (Gasto)", "Entrada (Ganho)"])
        d = st.text_input("Descrição")
        v = st.number_input("Valor R$", min_value=0.0)
        if st.form_submit_button("Adicionar"):
            val = v if t == "Entrada (Ganho)" else -v
            st.session_state.transacoes.append({"Data": date.today(), "Descrição": d, "Tipo": t, "Valor (R$)": val})
            st.rerun()

with st.sidebar.expander("📸 Subir PDF ou Print"):
    arquivo = st.file_uploader("Arraste aqui seu arquivo", type=["pdf", "png", "jpg", "jpeg"])
    if arquivo and st.button("Processar Agora"):
        if arquivo.type == "application/pdf":
            with pdfplumber.open(arquivo) as pdf:
                texto_total = ""
                for pagina in pdf.pages:
                    texto_total += pagina.extract_text() or ""
                processar_linhas_texto(texto_total, "PDF")
        else:
            # Processamento de Imagem (OCR)
            img = Image.open(arquivo)
            try:
                # Usa espanhol/português para ler os caracteres
                texto_ocr = pytesseract.image_to_string(img, lang='spa+por') 
                processar_linhas_texto(texto_ocr, "PRINT")
            except Exception as e:
                st.error(f"Erro ao ler imagem: {e}. Verifique o Tesseract no Windows.")
        st.sidebar.success("Processado com sucesso!")

# --- 4. PAINEL PRINCIPAL ---
st.title("📊 Painel de Controle de Gastos")

if st.session_state.transacoes:
    df = pd.DataFrame(st.session_state.transacoes)
    
    entradas = df[df['Valor (R$)'] > 0]['Valor (R$)'].sum()
    saidas = abs(df[df['Valor (R$)'] < 0]['Valor (R$)'].sum())
    saldo = entradas - saidas

    # Métricas com as cores da Adriana
    c1, c2, c3 = st.columns(3)
    c1.metric("Entradas (Ouro)", f"R$ {entradas:,.2f}")
    c2.metric("Saídas (Militar)", f"R$ {saidas:,.2f}")
    c3.metric("Saldo Atual", f"R$ {saldo:,.2f}")

    col_tabela, col_grafico = st.columns([2, 1])

    with col_tabela:
        st.subheader("📋 Histórico")
        st.dataframe(df, use_container_width=True)
        if st.button("🗑️ Limpar Tudo"):
            st.session_state.transacoes = []
            st.rerun()

    with col_grafico:
        st.subheader("🍩 Distribuição")
        df_pizza = pd.DataFrame({"Tipo": ["Entradas", "Saídas"], "Valor": [entradas, saidas]})
        st.vega_lite_chart(df_pizza, {
            'mark': {'type': 'arc', 'innerRadius': 50},
            'encoding': {
                'theta': {'field': 'Valor', 'type': 'quantitative'},
                'color': {
                    'field': 'Tipo', 
                    'type': 'nominal', 
                    'scale': {'range': [COR_OURO, COR_VERDE_MILITAR]}
                }
            }
        }, use_container_width=True)
else:
    st.info("Olá, Adriana! Suba um PDF de resumo ou um print de comprovante na barra lateral para começar.")