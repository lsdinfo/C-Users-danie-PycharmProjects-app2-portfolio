import streamlit as st
from send_email import send_email
import pandas

st.header("Contact Me")

df = pandas.read_csv(".venv/topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Enter yuor email address:")
    topic_txt = st.selectbox("What topic do you want to discuss: ",
                             df["topic"])
    txt_message = st.text_area("Enter your message:", height=100)
    button = st.form_submit_button("Submit")

    message = f"""\
Subject: new email from: {user_email}

From: {user_email}
Topic: {topic_txt}
{txt_message}
"""
    if button:
        send_email(message)
        st.info("Email has been sent.")








