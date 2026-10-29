from typing import Optional

import streamlit as st
from backend.haiku import Haiku
from backend.hub import Hub
from backend.user import User


@st.dialog("Haiku editor", width="large")
def haiku_editor(hub: Hub, user: User, haiku: Optional[Haiku] = None) -> None:
    haiku_text = st.text_area(
        "Enter a haiku",
        value=haiku.text if haiku else "",
    )

    if st.button("Save haiku", type="primary"):
        if haiku:
            new_haiku = hub.haiku_service.update_haiku(haiku.haiku_id, haiku_text)
        else:
            new_haiku = hub.haiku_service.create_haiku(user.username, haiku_text)

        if new_haiku:
            st.success("Haiku saved successfully!")
            st.rerun()
        else:
            st.error("Failed to save haiku")
