import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv("data.csv")
planets= data.columns[1:]


# mass= data.values[0]
# wd=mass[1:].astype(float)

# plt.bar(planets,wd)
# plt.show()

i= int(input("Enter What You Want to See: "))

def bar():
    y=data.values[i-1]
    atx= y[1:].astype(float)

    plt.bar(planets,atx)
    plt.xticks(rotation=-45)
    plt.show()


bar()