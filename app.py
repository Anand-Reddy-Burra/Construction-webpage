import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Construction Website",
    page_icon="🏗️",
    layout="wide"
)

html_file = Path("index.html")
css_file = Path("styles.css")
js_file = Path("script.js")

html = html_file.read_text(encoding="utf-8")
css = css_file.read_text(encoding="utf-8")
js = js_file.read_text(encoding="utf-8")

# Inject CSS
html = html.replace(
    "</head>",
    f"<style>{css}</style></head>"
)

# Inject JavaScript
html = html.replace(
    "</body>",
    f"<script>{js}</script></body>"
)

st.components.v1.html(
    html,
    height=1200,
    scrolling=True
)
