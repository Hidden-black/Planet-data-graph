import streamlit as st
import pdata as pa

home= st.Page(
    "web.py",
    title="Home",
    icon=":material/home:"
)

st.logo("https://us-east-1.tixte.net/uploads/hiddenblack.tixte.co/Code_Tkf1Xuu3Xp.png")
st.image("https://us-east-1.tixte.net/uploads/hiddenblack.tixte.co/Code_Tkf1Xuu3Xp.png")
st.markdown("""
The Data in this has been obtained from [NASA](https://nssdc.gsfc.nasa.gov/planetary/factsheet/)
            """)
st.markdown("Anydata that is unknown has been replaced with 0.")
st.divider()

st.link_button("Raw Data","/data",help="Look at Raw Data", type="secondary", icon="📑", disabled=False, use_container_width=False)
st.link_button("Plot Graph","/graph",help="Plot Various Graphs", type="secondary", icon="📊", disabled=False, use_container_width=False)
st.link_button("Analyse Data","/analyse",help="Arange Data In Diffrent Order", type="secondary", icon="🤔", disabled=False, use_container_width=False)

st.divider()
st.markdown("[Report Bugs](https://github.com/Hidden-black/Planet-data-graph/issues/)")