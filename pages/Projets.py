import os
import streamlit as st

from Accueil import my_sidebar


def st_write_file(filename: str):
    filepath = os.path.join("docs", "projets", filename)
    with open(filepath, 'rt', encoding='utf-8') as file:
        st.markdown(file.read())


my_sidebar()

st.title("Projets")

with st.expander("Stage"):
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