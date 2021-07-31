import csv
import pandas as pd

df=pd.read_csv("ProjectFinalMerged.csv")
print(df.shape)

del df['Distance']

del df['Mass']

del df['Radius']

del df['Star_name']

# print(list(df))

df.to_csv('Projectmain.csv')