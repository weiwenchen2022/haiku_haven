import streamlit as st
from backend.hub import Hub
from backend.user import User
from frontend.haiku_display import display_haiku
from frontend.haiku_editor import haiku_editor
from frontend.icons import Icons

hub: Hub = st.session_state.hub
user: User = st.session_state.user

st.title(f"Welcome, {user.username}")

if st.button(f"{Icons.ADD} Haiku", type="primary"):
    haiku_editor(hub, user)

st.header(f"{user.username}'s haikus", divider="grey")


if haikus := hub.haiku_service.get_haikus_by_author(user.username):
    for haiku in haikus:
        display_haiku(haiku)
else:
    st.info("You haven't written any haikus yet.")
