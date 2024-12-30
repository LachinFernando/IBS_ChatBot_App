import streamlit as st

from utils import create_post_payload, ibs_signin


IMAGE_ADDRESS = "https://www.researchgate.net/publication/370767314/figure/fig1/AS:11431281211563079@1702429292171/Therapeutic-and-nutritional-management-of-irritable-bowel-syndrome.tif"


# web app
st.title("IBS Nutrition Guider")
st.image(IMAGE_ADDRESS, caption = "IBS Nutrition")

st.header("Please Sign In")

with st.form("SignIn Form"):
    username = st.text_input("UserEmail", placeholder = "Enter your Email Address")
    password = st.text_input("Password", placeholder = "Enter your password", type = "password")
    re_enter_password = st.text_input("Re-Enter Your Password", placeholder = "Enter your password", type = "password")

    submitted = st.form_submit_button("SignIn")
    if submitted:
        if username and password:
            if password != re_enter_password:
                st.error("Passwords are not macthing. Please check!", icon = "🚨")
                st.stop()
            with st.spinner("Processing......."):
                payload = create_post_payload(username, password)
                signin_response = ibs_signin(payload)
            if signin_response["status"] == "failure":
                st.error(signin_response["errors"][0], icon = "🚨")
            else:
                st.session_state.login = False
                st.success("SignIn Successful! Please log in to the app from LogIn Page!", icon = "✅")
        else:
            st.error("Please enter your username or password", icon = "🚨")