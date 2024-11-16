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

by, bn= st.columns(2)

bl = True
with by:
    if st.button("With Values"):
        bl = True

with bn:
    if st.button("Without Values"):
        bl = False

fig, ax= plt.subplots()

if ptype == "Bar" and bl == False:
    ax.bar(pa.dT.index,pa.dT[dtype],color='c')
    ax.set_title(f"{dtype} of Planets")
    ax.set_xlabel("Planets")
    ax.set_xticklabels(pa.dT.index,rotation=45,ha="right")
    ax.set_ylabel(ptype)
    ax.get_tightbbox()

elif ptype == "Line" and bl == False:
    ax.plot(pa.dT.index,pa.dT[dtype],color='c',marker='o')
    ax.set_title(f"{dtype} of Planets")
    ax.set_xlabel("Planets")
    ax.set_ylabel(ptype)
    ax.set_xticklabels(pa.dT.index,rotation=45,ha="right")
    ax.get_tightbbox()
    
elif ptype == "Pie":
    wedges, texts, autotexts = ax.pie(
        pa.dT[dtype],
        labels=pa.dT.index,
        autopct='%1.1f%%',
        startangle=140,
        pctdistance=0.85,
        labeldistance=1.1
    )
    ax.set_title(f"{dtype} of Planets")
    
    for text in texts:
        text.set_fontsize(10)
        text.set_rotation(30)
    
    for autotext in autotexts:
        autotext.set_fontsize(9)


if ptype == "Bar" and bl== True:
    bars = ax.bar(pa.dT.index, pa.dT[dtype], color='c')
    ax.set_title(f"{dtype} of Planets")
    ax.set_xlabel("Planets")
    ax.set_xticklabels(pa.dT.index, rotation=45, ha="right")
    ax.set_ylabel(ptype)
    
    for bar, value in zip(bars, pa.dT[dtype]):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                f'{value:.2f}', ha='center', va='bottom', fontsize=10)

elif ptype == "Line" and bl == True:
    ax.plot(pa.dT.index, pa.dT[dtype], color='c', marker='o')
    ax.set_title(f"{dtype} of Planets")
    ax.set_xlabel("Planets")
    ax.set_ylabel(ptype)
    ax.set_xticklabels(pa.dT.index, rotation=45, ha="right")

    for x, y in zip(pa.dT.index, pa.dT[dtype]):
        ax.text(x, y, f'{y:.2f}', ha='center', va='bottom', fontsize=10)

st.pyplot(fig)