import os
import streamlit as st


def st_write_content(content: str):

    textblock = [elt for elt in content.split("<img>") if elt and elt!="\n"]

    if len(textblock) > 1:
        col1, col2 = st.columns(2)
        for block in textblock[0::2]:
            if block.startswith("img/"):
                img, caption, width = block.split("|")
                width = int(width) if width else None
                col1.image(img, caption=caption, width=width)
            else:
                col1.markdown(block)

        for block in textblock[1::2]:
            if block.startswith("img/"):
                img, caption, width = block.split("|")
                width = int(width) if width else None
                col2.image(img, caption=caption, width=width)
            else:
                col2.markdown(block)

    else:
        for block in textblock:
            if block.startswith("img/"):
                img, caption, width = block.split("|")
                width = int(width) if width else None
                st.image(img, caption=caption, width=width)
            else:
                st.markdown(block)


def st_write_select(filename: str):
    filepath = os.path.join("docs", "projets", filename)
    with open(filepath, 'rt', encoding='utf-8') as file:
        content = file.read().split("# ")
    keys = [s[:s.find('\n')] for s in content]
    values = [s[s.find('\n')+len('\n'):] for s in content]
    text_parts = dict(zip(keys, values))
    text = st.selectbox(
        keys[0], 
        tuple(list(text_parts.keys())[1:])
    )
    st_write_content(text_parts[text])


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
    st_write_select("stage.txt")
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

# with st.expander("Projet OpenData"):
#     st_write_file("open_data.txt")
#     st.link_button("Voir le rapport d'analyse", "docs/FACCI_NGUYEN_rapport_projetOpenData.html")

# with st.expander("Prédiction de prix d'hôtels"):
#     st_write_file("1001_hotels.txt")

# with st.expander("Root"):
#     if st.checkbox("Expand"):
#         st.write("Hurray !")
    