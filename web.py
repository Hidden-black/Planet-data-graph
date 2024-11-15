import streamlit as st
import pdata as pa

home= st.Page(
    "web.py",
    title="Home",
    icon=":material/home:"
)

st.image("https://us-east-1.tixte.net/uploads/hiddenblack.tixte.co/Code_Tkf1Xuu3Xp.png")
st.markdown("""
The Data in this has been obtained from [NASA](https://nssdc.gsfc.nasa.gov/planetary/factsheet/)
            """)
st.markdown("Anydata that is unknown has been replaced with 0.")
st.divider()

st.link_button("Plot Graph","/Graph",help="Plot Various Graphs", type="secondary", icon="📊", disabled=False, use_container_width=False)
st.link_button("Analyse Data","/Analyse",help=None, type="secondary", icon="🤔", disabled=False, use_container_width=False)