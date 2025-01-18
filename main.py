import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image(".venv/Images/photo.png")

with col2:
    st.title("Daniele Santagati")
    content = """
    Ciao mi chiamo Daniele e sono un cicloviaggiatore
    in lunghe distanze. Il mio prossimo viaggio sarà
    in Giappone con un itinerario che da Kyoto mi
    porterà a Tokyo.
    """

    st.info(content)


content2 = """
Belowe you can find some of my apps I have built in Python. Feel free to contact me.
"""
st.write(content2)



