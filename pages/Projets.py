import os
import streamlit as st


def st_write_file(filename: str):
    filepath = os.path.join("docs", "projets", filename)
    with open(filepath, 'rt', encoding='utf-8') as file:
        st.markdown(file.read())


st.set_page_config(
    page_title="Portefolio/Projets",
    page_icon="🗃️",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .stMarkdown {
        text-align: justify;
    }
</style>
""", unsafe_allow_html=True)

st.sidebar.header('NGUYEN Alexandre')
st.sidebar.markdown("""
📞 : 06.33.92.62.05

📧 : alex33nguyen@gmail.com
""")
with open("docs/_CV_Alex.pdf", 'rb') as file:
    st.sidebar.download_button(
        label='Télécharger mon CV', 
        data=file.read(), 
        file_name="CV_Alexandre_NGUYEN.pdf"
        )

c1, c2 = st.sidebar.columns(2)
c1.markdown("""
[![Profil LinkedIn](https://img.icons8.com/fluency/48/linkedin.png)](https://www.linkedin.com/in/alexandre-nguyen-716394247/)
""")
c2.markdown("""
[![Page GitHub](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/ASNguyen8)
""")

st.title("Projets")

with st.expander("Stage de fin de master (du 20 Février 2023 au 20 Juillet 2023)"):
    st_write_file("stage.txt")
    stage1, stage2 = st.columns(2)
    with open("docs/Rapport_stage.pdf", 'rb') as file:
        stage1.download_button(
            label='Rapport de stage', 
            data=file.read(), 
            file_name="rapport_stage_Alexandre_NGUYEN.pdf"
            )
    with open("docs/soutenance_finale.pdf", 'rb') as file:
        stage2.download_button(
            label='Diapo soutenance de stage',
            data=file.read(), file_name="soutenance_stage_Alexandre_NGUYEN.pdf"
            )

with st.expander("Projet OpenData"):
    st_write_file("open_data.txt")
    st.link_button("Voir le rapport d'analyse", "docs/FACCI_NGUYEN_rapport_projetOpenData.html")

with st.expander("Prédiction de prix d'hôtels"):
    st_write_file("1001_hotels.txt")