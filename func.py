import pandas as pd
import matplotlib.pyplot as plt
data= pd.read_csv("data.csv")
planets= data.columns[1:]

def bar(i):
    y=data.values[i-1]
    atx= y[1:].astype(float)
    label=y[0]
    plt.bar(planets,atx,marker="8",color="c")
    plt.xlabel("Planets")
    plt.xticks(rotation=45)
    plt.ylabel(f"{label}",rotation=90)
    plt.title(f"{label} of Planets")
    plt.show()

def point(i):
    y=data.values[i-1]
    atx= y[1:].astype(float)
    label=y[0]
    plt.plot(planets,atx,marker="8",color="c")
    plt.xlabel("Planets")
    plt.xticks(rotation=45)
    plt.ylabel(f"{label}",rotation=90)
    plt.title(f"{label} of Planets")
    plt.show()



def avail_data():
    print("""
    1. Mass(10^24kg)                    11. Orbital Period(days)
    2. Diameter(km)                     12. Orbital Velocity(km/s)
    3. Density(kg/m3)                   13. Orbital Inclination(degrees)
    4. Gravity(m/s2)                    14. Orbital Eccentricity
    5. Escape Velocity(km/s)            15. Obliquity to Orbit(degrees)
    6. Rotation Period(hours)           16. Mean Temperature(C)
    7. Length of Day(hours)             17. Surface Pressure(bars)
    8. Distance from Sun(10^6km)        18. Number of Moons
    9. Perihelion(10^6km)               19. Ring System
    10. Aphelion(10^6km)                20. Global Magnetic Field
    """)
    pass




def mainmenu():
    print("""
-------------------------------------
    1. Display Data
    2. Display Graph
    3. Analyze Data
    4. Exit
-------------------------------------
        """)
    
    uinp= int(input("Enter:"))

    if uinp>=1 and uinp <=5:
        if uinp==1:
            disp_data()
        elif uinp==2:
            pass
        elif uinp==3:
            pass
        elif uinp==4:
            exit()
    else:
        print("Invalid Input")
        mainmenu()


def exit():
    breakpoint

def disp_data():
    print(data)
    print("_______________________________________\n")
    mainmenu()

def analyse():
    print("""
-------------------------------------
    1. Display Maximum Value 
    2. Display Minimum Value
    3. Display Data Of A Planet
    4. Exit
-------------------------------------
        """)
    
    ainp= int(input("Enter:"))

    if ainp>=1 and ainp <=5:
        if ainp==1:
            pass
        elif ainp==2:
            pass
        elif ainp==3:
            pass
        elif ainp==4:
            exit()
    else:
        print("Invalid Input")
        analyse()