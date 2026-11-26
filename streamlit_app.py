"""Render the Durham post-storm electrical guide."""

from base64 import b64encode
from pathlib import Path

import streamlit as st


APP_DIR = Path(__file__).resolve().parent

st.set_page_config(
    page_title="Partial Power After a Storm in Durham, NC",
    layout="wide",
    initial_sidebar_state="collapsed",
)

guide = (APP_DIR / "guide.html").read_text(encoding="utf-8")
image = b64encode((APP_DIR / "durham-after-the-storm.webp").read_bytes()).decode("ascii")
st.html(guide.replace("{{ HERO_IMAGE }}", f"data:image/webp;base64,{image}"))
