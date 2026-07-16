import streamlit as st

st.title("MISES WOOOOOOO")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
number = st.number_input("Nombre de dés")
st.write("Current num : " + number)
