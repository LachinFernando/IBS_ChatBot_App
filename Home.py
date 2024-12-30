import streamlit as st

from utils import create_get_payload, login


IMAGE_ADDRESS = "https://www.researchgate.net/publication/370767314/figure/fig1/AS:11431281211563079@1702429292171/Therapeutic-and-nutritional-management-of-irritable-bowel-syndrome.tif"


if 'login' not in st.session_state:
    st.session_state.login = False

# web app
st.title("IBS Nutrition Guider")
st.image(IMAGE_ADDRESS, caption = "IBS Nutrition")

st.header("Please Log In")

with st.form("LogIn Form"):
    username = st.text_input("UserEmail", placeholder = "Enter your Email Address")
    password = st.text_input("Password", placeholder = "Enter your password", type = "password")

    submitted = st.form_submit_button("LogIn")
    if submitted:
        if username and password:
            with st.spinner("Processing......."):
                payload = create_get_payload(username, password)
                login_response = login(payload)
            if login_response["status"] == "failure":
                st.error(login_response["errors"][0], icon = "🚨")
            else:
                st.session_state.login = True
                st.success("LogIn Successful!", icon = "✅")
        else:
            st.error("Please enter your username or password", icon = "🚨")