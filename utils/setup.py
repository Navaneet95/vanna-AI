import os
import streamlit as st
import vanna as vn
from dotenv import load_dotenv


@st.cache_resource(ttl=3600)
def setup_connexion():
    if "vanna_api_key" in st.secrets and "url" in st.secrets:
        vn.set_api_key(st.secrets.get("vanna_api_key"))
        vn.set_model("vanna-increff-ai")
        vn.connect_to_sqlite(
            host=st.secrets.get("url"),

        )

    else:
        load_dotenv()
        vn.set_api_key(os.environ.get("VANNA_API_KEY"))
        vn.set_model("vanna-increff-ai")
        vn.connect_to_sqlite(
            url=os.environ.get("url"),
        )


def setup_session_state():
    st.session_state["my_question"] = None
