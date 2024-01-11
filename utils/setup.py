import os
import streamlit as st
import vanna as vn
from dotenv import load_dotenv


@st.cache_resource(ttl=3600)
def setup_connexion():
    if "vanna_api_key" in st.secrets and "host" in st.secrets:
        vn.set_api_key(st.secrets.get("vanna_api_key"))
        vn.set_model("vanna-increff-demo")
        vn.connect_to_postgres(
            host=st.secrets.get("host"),
            dbname=st.secrets.get("dbname"),
            user=st.secrets.get("user"),
            password=st.secrets.get("password"),
            port=st.secrets.get("port"),

        )

    else:
        load_dotenv()
        vn.set_api_key(os.environ.get("VANNA_API_KEY"))
        vn.set_model("vanna-increff-demo")
        vn.connect_to_postgres(
            host=os.environ.get("host"),
            dbname=os.environ.get("dbname"),
            user=os.environ.get("user"),
            password=os.environ.get("password"),
            port=os.environ.get("port"),
        )


def setup_session_state():
    st.session_state["my_question"] = None
