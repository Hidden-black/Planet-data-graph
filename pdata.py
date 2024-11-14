import pandas as pd

datai= {
    "Mercury":[0.33,4879,5429,3.7,4.3,1407.6,4222.6,57.9,46,69.8,88,47.4,7,0.206,0.034,167,0,0,0,0],
    "Venus":[4.87,12104,5243,8.9,10.4,-5832.5,2802,108.2,107.5,108.9,224.7,35,3.4,0.007,177.4,464,92,0,0,0],
    "Earth":[5.97,12756,5514,9.8,11.2,23.9,24,149.6,147.1,152.1,365.2,29.8,0,0.017,23.4,15,1,1,0,1],
    "Mars":[0.642,6792,3934,3.7,5,24.6,24.7,228,206.7,249.3,687,24.1,1.8,0.094,25.2,-65,0.01,2,0,0],
    "Jupiter":[1898,142984,1326,23.1,59.5,9.9,9.9,778.5,740.6,816.4,4331,13.1,1.3,0.049,3.1,-110,0,95,1,1],
    "Saturn":[568,120536,687,9,35.5,10.7,10.7,1432,1357.6,1506.5,10747,9.7,2.5,0.052,26.7,-140,0,146,1,1],
    "Uranus":[86.8,51118,1270,8.7,21.3,-17.2,17.2,2867,2732.7,3001.4,30589,6.8,0.8,0.047,97.8,-195,0,28,1,1],
    "Neptune":[102,49528,1638,11,23.5,16.1,16.1,4515,4471.1,4558.9,59800,5.4,1.8,0.01,28.3,-200,0,16,1,1],
    "Pluto":[0.013,2376,1850,0.7,1.3,-153.3,153.3,5906.4,4436.8,7375.9,90560,4.7,17.2,0.244,119.5,-225,0.00001,5,0,0]
}

ind=["Mass (10²⁷kg)","Diameter (km)","Density (kg/m³)","Gravity (m/s²)"
     ,"Escape Velocity (km/s)","Rotation Period (hours)","Length of Day (hours)"
     ,"Distance from Sun (10⁶km)","Perihelion (10⁶km)","Aphelion (10⁶km)","Orbital Period (days)"
     ,"Orbital Velocity (km/s)","Orbital Inclination (degrees)","Orbital Eccentricity"
     ,"Obliquity to Orbit (degrees)","Mean Temperature (C)","Surface Pressure (bars)"
     ,"Number of Moons","Ring System","Global Magnetic Field"]

data= pd.DataFrame(datai,index=ind)
planets= data.columns[1:]
dT= data.T
dtypes=dT.columns[1:]
