import streamlit as st
import pandas as pd
import pdata as pa

st.set_page_config(page_title="Anaylyse")
st.image("https://us-east-1.tixte.net/uploads/hiddenblack.tixte.co/Code_Tkf1Xuu3Xp.png")
st.divider()

st.markdown("""
The Data in this has been obtained from [NASA](https://nssdc.gsfc.nasa.gov/planetary/factsheet/)
            """)
st.markdown("Anydata that is unknown has been replaced with 0.")
st.divider()


dtype=st.selectbox("Choose the data type to plot: ",pa.ind)
ptype=st.radio("Choose Anaylyse type: ",["Ascending","Descending","Maximum","Minimum"])

st.markdown(dtype)
# lm= pa.data.columns.get_loc(f"{dtype}")


def lma(imp):
    st.markdown(pa.data.values[1])
    de= pd.Series(pa.planets)

if ptype == "Ascending":
    lma(dtype)
    
    # st.markdown(f"{de.idxmax()} Has Highest {max(de)} {x[0]}")
    pass

elif ptype == "Descending":
    pass

elif ptype == "Maximum":

    pass

elif ptype == "Minimum":
    pass