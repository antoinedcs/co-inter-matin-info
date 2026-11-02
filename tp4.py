import random
import pandas as pd

df = pd.read_csv('dataSpeed.csv')

df["danger"] = df["danger"].map({False: 0, True: 1})

X = df["Vitesse"].tolist()
Y = df["danger"].tolist()

W = random.randint(-10,10)
B = random.randint(-10,10)

def Zpredict(x):
    Z = W* x + B
    if Z >=0 :
        return 1
    else :
        return 0

