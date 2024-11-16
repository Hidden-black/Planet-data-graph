import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import pdata as pa


st.set_page_config(page_title="Planet Data")
st.image("https://us-east-1.tixte.net/uploads/hiddenblack.tixte.co/Code_Tkf1Xuu3Xp.png")

st.markdown("""
The Data in this has been obtained from [NASA](https://nssdc.gsfc.nasa.gov/planetary/factsheet/)
            """)
st.markdown("Anydata that is unknown has been replaced with 0.")
st.divider()
plt.style.use('dark_background')
dtype=st.selectbox("Choose the data type to plot: ",pa.ind)
ptype=st.radio("Choose Plot type: ",["Bar","Line","Pie"])

fig, ax= plt.subplots()

if ptype == "Bar":
    ax.bar(pa.dT.index,pa.dT[dtype],color='c')
    ax.set_title(f"{dtype} of Planets")
    ax.set_xlabel("Planets")
    ax.set_xticklabels(pa.dT.index,rotation=45,ha="right")
    ax.set_ylabel(ptype)
    ax.get_tightbbox()

elif ptype == "Line":
    ax.plot(pa.dT.index,pa.dT[dtype],color='c',marker='o')
    ax.set_title(f"{dtype} of Planets")
    ax.set_xlabel("Planets")
    ax.set_ylabel(ptype)
    ax.set_xticklabels(pa.dT.index,rotation=45,ha="right")
    ax.get_tightbbox()
    
elif ptype == "Pie":
    ax.pie(pa.dT[dtype],labels=pa.dT.index,autopct='%1.1f%%',
           startangle=140)
    ax.set_title(f"{dtype} of Planets")
st.pyplot(fig)