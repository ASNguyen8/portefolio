import streamlit as st
import datetime

st.set_page_config(
    page_title="Portefolio",
    page_icon="🗃️",
    initial_sidebar_state="expanded"
)

today = datetime.datetime.today()
birth = datetime.datetime(year=1998, month=1, day=8, hour=22, minute=15)
age = ((today-birth).days - len([year for year in range(birth.year, today.year+1) if year%4 == 0])) // 365

# Sidebar elements
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


# Description
st.markdown("# NGUYEN Alexandre")
coord, photo = st.columns([0.75, 0.25])
coord.markdown(f"{age} ans")
with open("docs/presentation/coordonnees.txt", 'rt', encoding='utf-8') as file:
    coord.markdown(file.read())

photo.image("img/photo_rognee.jpg")

st.title("Présentation")
with open("docs/presentation/description.txt", 'rt') as file:
    st.markdown(file.read())
