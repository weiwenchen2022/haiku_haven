import streamlit as st
from backend.haiku import Haiku
from backend.hub import Hub
from backend.user import User
from frontend.haiku_editor import haiku_editor
from frontend.icons import Icons

hub: Hub = st.session_state.hub
user: User = st.session_state.user


def display_haiku(haiku: Haiku) -> None:
    with st.container(border=True):
        created_col, text_col, edit_col, delete_col = st.columns([2, 5, 1, 1])
        with created_col:
            st.markdown(get_haiku_created_display(haiku))

        with text_col:
            st.markdown(get_haiku_text_display(haiku))

        with edit_col:
            edit_button(haiku)

        with delete_col:
            delete_button(haiku)


def get_haiku_created_display(haiku: Haiku) -> str:
    day = haiku.created_at.strftime("%Y-%m-%d")
    time = haiku.created_at.strftime("%H:%M")
    return f":gray[{Icons.CALENDAR} {day}  \n {Icons.CLOCK} {time}]"


def get_haiku_text_display(haiku: Haiku) -> str:
    display_text = haiku.text.replace("\n", "  \n")
    return f":green[{display_text}]"


def edit_button(haiku: Haiku):
    if st.button(f"{Icons.EDIT}", key=f"edit_{haiku.haiku_id}"):
        haiku_editor(hub, user, haiku)


def delete_button(haiku: Haiku):
    if st.button(f"{Icons.DELETE}", key=f"delete_{haiku.haiku_id}"):
        deleted_haiku = hub.haiku_service.delete_haiku(haiku.haiku_id)
        if deleted_haiku:
            st.rerun()
        else:
            st.error("Failed to delete haiku.")
