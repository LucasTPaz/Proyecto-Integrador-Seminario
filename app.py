import streamlit as st


st.set_page_config(page_title="Mi app de Streamlit", page_icon="🚀")

st.title("Mi primera app con Streamlit")
st.write("Una aplicación mínima lista para personalizar.")

nombre = st.text_input("¿Cómo te llamas?")

if st.button("Saludar"):
    if nombre.strip():
        st.success(f"¡Hola, {nombre.strip()}!")
    else:
        st.warning("Escribe tu nombre para recibir un saludo.")