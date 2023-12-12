import os
import streamlit as st


def st_write_file(filename: str):
    filepath = os.path.join("docs", "formations", filename)
    with open(filepath, 'rt', encoding='utf-8') as file:
        st.markdown(file.read())


st.set_page_config(
    page_title="Portefolio/Formations",
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

st.title("Formations")
with st.expander("2021 - 2023 : Master MAS, parcours CMI ISI"):
    st_write_file("master.txt")

with st.expander("2018 - 2021 : Licence Mathématiques, parcours CMI ISI"):
    st_write_file("licence_info.txt")

with st.expander("2016 - 2018 : PACES"):
    st_write_file("paces.txt")

with st.expander("2016 : Bac S"):
    st_write_file("bac.txt")

st.title("CMI ISI")

with st.expander("Cursus Master Ingénierie, Ingénierie de la Statistique et de l'Informatique"):
    st_write_file("cmi_isi.txt")

st.title("Autres diplômes/certificats")
st_write_file('autres_diplomes.txt')