import pandas as pd
import matplotlib.pyplot as plt
data= pd.read_csv("data.csv")
planets= data.columns[1:]

def bar(i):
    y=data.values[i-1]
    atx= y[1:].astype(float)
    label=y[0]
    plt.bar(planets,atx)
    plt.xlabel("Planets")
    plt.xticks(rotation=45)
    plt.ylabel(f"{label}",rotation=90)
    plt.title(f"{label} of Planets")
    plt.show()

def point(i):
    y=data.values[i-1]
    atx= y[1:].astype(float)
    label=y[0]
    plt.plot(planets,atx)
    plt.xlabel("Planets")
    plt.xticks(rotation=45)
    plt.ylabel(f"{label}",rotation=90)
    plt.title(f"{label} of Planets")
    plt.show()