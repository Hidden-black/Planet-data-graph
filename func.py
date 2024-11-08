try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import os
    import time
except ModuleNotFoundError:
    print("Some Modules are not installed")
    print("Installing...")
    os.system('pip install -r requirements.txt')
    print("Done")
    time.sleep(2)
    os.system('cls')
    

data= pd.read_csv("data.csv")
planets= data.columns[1:]

def mainmenu():
    print("""
-------------------------------------
    1. Display Data
    2. Display Graph
    3. Analyze Data
    4. Exit
-------------------------------------
        """)
    
    uinp= int(input("Enter your choice:"))

    if uinp>=1 and uinp <=4:
        if uinp==1:
            disp_data()
        elif uinp==2:
            avail_data()
            i= int(input("Enter what kind of data you want: "))
            if i==6 or i==16 or i==17:
                point(i)
            elif i==19 or i==20:
                point_bool(i)
            else:
                
                print("""
    1. Line Graph
    2. Bar Graph
    3. Pie Chart
                      """)
                k_og(i)

        elif uinp==3:
            analyse()
        elif uinp==4:
            exit()
    else:
        print("Invalid Input")
        mainmenu()

def disp_data():
    print(data)
    mainmenu()

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

def exit():
    breakpoint

def bar(i):
    y=data.values[i-1]
    atx= y[1:].astype(float)
    label=y[0]
    plt.bar(planets,atx,color="c")
    plt.xlabel("Planets")
    plt.xticks(rotation=45)
    plt.ylabel(f"{label}",rotation=90)
    plt.title(f"{label} of Planets")
    plt.show()
    os.system('cls')
    mainmenu()


def point(i):
    y=data.values[i-1]
    atx= y[1:].astype(float)
    label=y[0]
    plt.plot(planets,atx,marker="8",color="c")
    plt.xlabel("Planets")
    plt.xticks(rotation=45)
    plt.ylabel(f"{label}",rotation=90)
    plt.title(f"{label} of Planets")
    save_graph()
    plt.show()
    os.system('cls')
    mainmenu()

def point_bool(i):
    y=data.values[i-1]
    atx= y[1:].astype(float)
    label=y[0]
    plt.plot(planets,atx,marker="8",color="c")
    plt.xlabel("Planets")
    plt.xticks(rotation=45)
    plt.ylabel(f"Yes/No",rotation=90)
    plt.ylim(-1,2)
    plt.title(f"{label} of Planets")
    plt.show()
    os.system('cls')
    mainmenu()

def pie_chart(i):
    y = data.values[i-1]
    values = y[1:].astype(float)
    label = y[0]
    
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=planets, autopct='%1.1f%%', startangle=140)
    plt.title(f"{label} Distribution Among Planets")
    plt.show()
    os.system('cls')
    mainmenu()

def k_og(i):
    last= int(input("Enter:"))
    if last ==1:
        point(i)
    elif last ==2:
        bar(i)
    elif last ==3:
        pie_chart(i)
    else:
        print("Invalid Input")
        k_og()

def analyse():
    print("""
-------------------------------------
    1. Display Maximum Value 
    2. Display Minimum Value
    3. Exit
-------------------------------------
        """)
    
    ainp= int(input("Enter:"))
    if ainp>=1 and ainp <=5:
        if ainp==1 or ainp==2:
            avail_data()
            imp= int(input("Enter: "))
            x=data.values[imp-1]
            ximp=x[1:].astype(float)
            de= pd.Series(ximp,planets)

            if ainp==1:
                print(f"{de.idxmax()} Has Highest {max(de)} {x[0]}")
                mainmenu()
            else:
                print(f"{de.idxmin()} Has Lowest {min(de)} {x[0]}")
                mainmenu()
        elif ainp==3:
            exit()
    else:
        print("Invalid Input")
        analyse()

def save_graph():
    imp=input(("Do you want to save graph As png (y/n)?"))
    if imp== "Y" or imp== "y":
        plt.tight_layout()
        plt.savefig("test.png")
    else:
        breakpoint