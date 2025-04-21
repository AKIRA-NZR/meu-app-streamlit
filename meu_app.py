import streamlit as st

a = st.text_input("Você me ama?")
if a:
    if a.lower() == "sim":
        st.write("Eu também te amo chata :)")
    else:
        st.write("Diga que sim vagabunda")