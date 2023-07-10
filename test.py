from itertools import chain
import csv
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

with open("exp.txt", "r") as fin,\
    open("file.txt", "w") as fout:
    zipped = zip(*(line.rstrip().split() for line in fin))
    fout.write("\n".join(chain(*zipped)))

Titles=['EMPLOYER','JOB TITLE','BASE SALARY','LOCATION','SUBMIT DATE','START DATE']

df=pd.read_fwf('exp.txt')
df.to_csv('testcsv1.csv',index=None)
dfcsv=pd.read_csv('testcsv1.csv',names=Titles)
dfcsv = dfcsv.iloc[6:]

grouped = dfcsv.groupby(dfcsv.index // 6)
transposed_df = grouped.apply(lambda x: x.T.reset_index(drop=True).T).reset_index(drop=True)

# Write the transposed data back to the CSV file
transposed_df.to_csv('filename_transposed.csv', index=False)




transposed_df.to_excel('testfile.xlsx',index=None)


with open('exp.csv') as input, open('demo1.csv', 'w', newline='') as output:
     writer = csv.writer(output)
     for row in csv.reader(input):
         if any(field.strip() for field in row):
             writer.writerow(row)

df=df.assign(F ='')
print(df.columns)
print(df.columns)
