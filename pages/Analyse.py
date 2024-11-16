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


ci = pa.dT.columns.get_loc(dtype)
val= pa.data.values[ci]


series = pd.Series(val,pa.planets)
serD= pd.DataFrame(series)
serDT= serD.T
# st.dataframe(series)
# st.dataframe(serDT)
st.divider()

if ptype == "Ascending":
    st.subheader(f"Aranged Values In Ascending Order")
    st.markdown(dtype)
    acen= series.sort_values()
    st.dataframe(acen)
    pass

elif ptype == "Descending":
    st.subheader(f"Aranged Values In Descenfing Order")
    st.markdown(dtype)
    acen= series.sort_values()
    st.dataframe(acen)
    pass

elif ptype == "Maximum":
    st.subheader(f"{series.idxmax()} Has Highest {max(series)} {dtype}")
    pass

elif ptype == "Minimum":
    st.subheader(f"{series.idxmin()} Has Lowest {min(series)} {dtype}")