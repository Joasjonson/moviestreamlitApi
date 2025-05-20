import streamlit as st
from login.service import login


def login_page():
    st.title("Login Page")
    st.write("Please enter your credentials to log in.")

    username = st.text_input("Username")
    password = st.text_input(
        label="Password",
        type="password")

    if st.button("Login"):
        login(username=username,
              password=password)
        
