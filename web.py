import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv("data.csv")
planets= data.columns[1:]
dataT=data.T
dTC= dataT.columns[1:]
st.set_page_config(page_title="Planet Data")

st.title("Planet data visualization")

dtype=st.selectbox("Choose the data type to plot: ",["1Mass (10²⁷kg)",
"Diameter (km)",
"Density (kg/m³)",
"Gravity (m/s²)",
"Escape Velocity (km/s)",
"Rotation Period (hours)",
"Length of Day (hours)",
"Distance from Sun (10⁶km)",
"Perihelion (10⁶km)",
"Aphelion (10⁶km)",
"Orbital Period (days)",
"Orbital Velocity (km/s)",
"Orbital Inclination (degrees)",
"Orbital Eccentricity",
"Obliquity to Orbit (degrees)",
"Mean Temperature (C)",
"Surface Pressure (bars)",
"Number of Moons"
"Ring System",
"Global Magnetic Field"
])
ptype=st.radio("Choose Plot type: ",["Bar","Line","Pie"])

fig, ax= plt.subplots()
st.markdown()
