import time  # noqa: INP001, D100

import streamlit as st
from pages_.container import container_page
from pages_.freight import freight_page
from pages_.home import home_page
from streamlit import rerun

st.set_page_config(
    layout="wide",
    page_title="Ocean Inbound",
    page_icon="🚢",
)


if "user_id" not in st.session_state:
    st.session_state["user_id"] = None

if "user_credentials" not in st.session_state:
    st.session_state["user_credentials"] = None

if "page" not in st.session_state:
    st.session_state["page"] = "home"



if st.session_state["page"] == "home":
    st.sidebar.title("Menu")
    paginas = st.sidebar.selectbox(
        "Select a page",
        ["Home", "Container", "Freight"],
    )
    if paginas == "Home":
        home_page()
    elif paginas == "Container":
        container_page()
    elif paginas == "Freight":
        freight_page()

    else:
        st.write("Página não encontrada")