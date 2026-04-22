import streamlit as st

home_page = st.Page(
    page = "home.py",
    title= "Home Page",
    default= True
)
signin_page = st.Page( page= "signin.py", title="sign in")
signup_page = st.Page( page= "signup.py", title="sign up")
menu_page = st.Page( page= "menu.py", title="menu")
chatbot_page = st.Page( page= "chatbot.py", title="chat bot")


all_pages = st.navigation(
    pages= [home_page,signin_page,signup_page,chatbot_page,menu_page],
    position="top"
    
)

all_pages.run()