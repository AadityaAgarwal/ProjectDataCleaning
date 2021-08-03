import csv
import pandas as pd

df=pd.read_csv("ProjectFinalMerged.csv")
print(df.shape)

df.drop(['Unnamed: 0', 'Luminosity', 'Unnamed: 6', 'Star_name1', 'Distance1', 'Mass1', 'Radius1'],axis=1,inplace=True)
print(df.columns)
finalData=df.dropna()

finalData.to_csv('Projectmain.csv')
