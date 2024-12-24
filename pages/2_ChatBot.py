import streamlit as st


if 'login' not in st.session_state:
    st.session_state.login = False

    
if not st.session_state.login:
    st.error("Please LogIn using the Home page to use the chatbot", icon = "🚨")
    st.stop()

st.header("IBS ChatBot")