import streamlit as st


def display_buttons(filepath: str, ncols: int=4, emphasis: bool=False):

    with open(filepath, "rt", encoding='utf-8') as file:
        content = [elt for elt in set(file.read().split("\n")) if elt]
    
    btn_type = "primary" if emphasis else "secondary"

    content.sort()
    columns = st.columns(ncols)
    for i, elt in enumerate(content):
        columns[i%ncols].button(elt, use_container_width=True, type=btn_type)


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

st.header("Outils")
st.markdown("Sont listés ici tous les logiciels que j'ai pu maîtriser, notamment au cours de [ma formation](/Formations).")
display_buttons("docs/outils_competences/outils.txt")

st.header("Compétences")
st.markdown("### Hard Skills")
display_buttons("docs/outils_competences/hard_skills.txt", emphasis=True)
st.markdown("### Soft Skills")
display_buttons("docs/outils_competences/soft_skills.txt")