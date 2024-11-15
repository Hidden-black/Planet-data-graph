import streamlit as st
import pdata as pa


st.title("Main")
st.image("https://us-east-1.tixte.net/uploads/hiddenblack.tixte.co/Code_Tkf1Xuu3Xp.png")

st.markdown("""
The Data in this has been obtained from [NASA](https://nssdc.gsfc.nasa.gov/planetary/factsheet/)
            """)

st.markdown("Anydata that is unknown has been replaced with 0.")
st.divider()
st.dataframe(pa.data)