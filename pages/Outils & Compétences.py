import streamlit as st

st.set_page_config(
    page_title="Portefolio/Outils&Compétences",
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

st.title("Compétences")

st.title("Outils")