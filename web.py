import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Planet Data")

st.title("Planet Data")
st.markdown("""
The Data in this has been obtained from [NASA](https://nssdc.gsfc.nasa.gov/planetary/factsheet/)
            """)
st.markdown("Anydata that is unknown has been replaced with 0")


if st.button("Plot Graph"):
    st.session_state.page = "graph"