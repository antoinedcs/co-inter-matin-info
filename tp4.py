import random
import pandas as pd

df = pd.read_csv('dataSpeed.csv')

df["danger"] = df["danger"].map({False: 0, True: 1})

X = df["Vitesse"]
Y = df["danger"]

W = random.randint(-10,10)
B = random.randint(-10,10)

