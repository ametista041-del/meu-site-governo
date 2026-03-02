import streamlit as st
import os

# Configuração da página
st.set_page_config(page_title="Governe Sua História", layout="wide")

# Título Principal
st.title("Governe Sua História")
st.subheader("Uma jornada de autoconhecimento e superação")

# Caminho da pasta de imagens
# No GitHub, as imagens devem estar na mesma pasta ou em uma subpasta
img_folder = "imagens"

# Lista de capítulos e imagens (ajuste os nomes dos arquivos conforme necessário)
capitulos = {
    "Identidade": "identidade.jpg",
    "Superação": "superacao.jpg",
    "Fundação": "fundacao.jpg",
    "Governo": "governo.jpg"
}

# Criar colunas para as fotos
cols = st.columns(len(capitulos))

for i, (cap, img_name) in enumerate(capitulos.items()):
    with cols[i]:
        st.header(cap)
        try:
            # Tenta carregar a imagem
            img_path = os.path.join(img_folder, img_name)
            st.image(img_path, use_container_width=True)
            
            # Textos de cada capítulo
            if cap == "Identidade":
                st.write("""Houve um tempo em que o meu valor era medido pelo que eu fazia. Enquanto eu era 'útil' para a instituição, tinha um lugar. Mas, quando o meu casamento ruiu e o divórcio se tornou a minha realidade, o acolhimento deu lugar ao silêncio e ao julgamento.""")
            
            if cap == "Superação":
                st.write("""Fui deixada de lado e rotulada de 'desviada' num momento em que mais precisava de colo. Ali, no vazio do abandono, eu descobri que a minha fé não dependia de um desempenho, mas de uma Identidade.""")
            
            if cap == "Fundação":
                st.write("""Aquele deserto não foi o meu fim, foi a minha fundação. Foi onde forjei a consistência necessária para deixar de ser refém das expectativas alheias e passar a governar a minha própria rota.""")
            
            if cap == "Governo":
                st.write("""Hoje, a minha missão é ajudar mulheres que, tal como eu, se sentem perdidas entre o que o mundo espera e o que a alma grita. Aqui, não encontras apenas consolo, encontras uma bússola estratégica para o teu novo começo.
                
**Bem-vinda ao governo da tua própria história.**""")

        except Exception as e:
            st.error(f"Erro ao carregar a imagem {cap}: {e}")

# Rodapé
st.divider()
st.write("© 2026 Adriana - Todos os direitos reservados.")
