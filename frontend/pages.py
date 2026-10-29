import streamlit as st
from frontend.icons import Icons

pages = {
    "login": st.Page(
        "frontend/login.py",
        title="Log in",
        icon=Icons.LOGIN,
    ),
    "signup": st.Page(
        "frontend/signup.py",
        title="Sign up",
        icon=Icons.SIGNUP,
    ),
    "home": st.Page(
        "frontend/home.py",
        title="Home",
        icon=Icons.HOME,
    ),
    "logout": st.Page(
        "frontend/logout.py",
        title="Log out",
        icon=Icons.LOGOUT,
    ),
}
