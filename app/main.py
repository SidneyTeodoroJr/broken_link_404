# Dependências
import streamlit as st

from module.page import *
from module.style import *
from module.search import *

page()
css()

st.sidebar.image("app\img\images.png")

st.sidebar.write("""<p>Esse projeto foi proposto pela <a href="https://www.freehelper.com.br/" target="_blank">Freehelper</a>, uma plataforma social que conecta ONGs, pessoas habilidosas e empresas responsáveis para projetos de curto-prazo em diferentes áreas profissionais.
<p/>""", unsafe_allow_html=True) 

st.sidebar.markdown('<p id="About">© 2024 <a href="https://github.com/SidneyTeodoroJr" target="_blank">Sidney T. A. Junior</a> / Todos os direitos reservados.</p>', unsafe_allow_html=True)


st.write("<h1>Broken Link 404<h1/>", unsafe_allow_html=True)
st.write("<p>O projeto é uma ferramenta de verificação de links quebrados em páginas Web. <p/>", unsafe_allow_html=True)

url_pagina = st.text_input("Insira um URL para verificar: ", )

# Botão de Verificação
if st.button("Verificar"):
    # Chamada da função verificar_links_quebrados com o URL inserido
    links_quebrados = verificar_links_quebrados(url_pagina)
    # Exibir resultados
    st.write("Links Quebrados:")

    for link in links_quebrados:
        st.write(f'Link: {link[0]}')
        st.write(f'Elemento HTML: {link[1]}')
        st.write('---')

    # Salvar os links quebrados em um documento do Word
    nome_arquivo = 'app\doc\links_quebrados.docx'
    salvar_links_quebrados(links_quebrados, nome_arquivo)
    st.success('Pesquisa concluída, faça download do registro no botão abaixo:')

    # Botão de download
    with open(nome_arquivo, "rb") as file:
        btn = st.download_button(
            label="Download doc",
            data=file,
            file_name="links_quebrados.docx",
        )