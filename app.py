import streamlit as st
from ui import UIManager
from service import (
    AuthService,
    InventoryService,
    OrderService,
    AIChatAssistant
)

st.set_page_config(
    page_title="Sunshine Bakery",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #FFF7D6;
}

.block-container {
    padding-top: 2rem;
}

div[data-testid="stMetric"] {
    background-color: white;
    padding: 10px;
    border-radius: 12px;
    border: 1px solid #E6C96B;
}

.stButton button {
    background-color: #F4B400;
    color: black;
    border-radius: 10px;
    border: none;
    font-weight: bold;
}

.stButton button:hover {
    background-color: #E0A000;
    color: white;
}
</style>
""", unsafe_allow_html=True)

DEFAULT_SESSION = {
    "page": "login",
    "logged_in": False,
    "user": None,
    "messages": []
}

for key, value in DEFAULT_SESSION.items():
    if key not in st.session_state:
        st.session_state[key] = value

ui = UIManager(
    AuthService(),
    InventoryService(),
    OrderService(),
    AIChatAssistant()
)

ui.render_application()
