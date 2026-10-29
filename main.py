import streamlit as st
from backend.hub import Hub
from frontend.pages import pages

if "hub" not in st.session_state:
    st.session_state.hub = Hub()

if st.session_state.get("logged_in", False):
    page = st.navigation(
        [
            pages["home"],
            pages["logout"],
        ]
    )
else:
    page = st.navigation(
        [
            pages["login"],
            pages["signup"],
        ]
    )

page.run()
