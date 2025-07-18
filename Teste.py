import streamlit as st

a = st.text_input("Este código funciona?")
if a:
    if a.lower() == "sim":
        st.write("Sim. Está funcionando corretamente")
    else:
        st.write("Seu codigo não está funcionando")
