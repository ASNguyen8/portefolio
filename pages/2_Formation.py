import os
import streamlit as st

def st_write_file(filename: str):
    filepath = os.path.join("docs", "formations", filename)
    with open(filepath, 'rt', encoding='utf-8') as file:
        st.markdown(file.read())

st.title("Formations")
with st.expander("2021 - 2023 : Master MAS, parcours CMI ISI"):
    st_write_file("master.txt")

with st.expander("2018 - 2021 : Licence Informatique, parcours CMI ISI"):
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