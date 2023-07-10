from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import csv
import numpy as np

#request data base from h1b1 website

getter=requests.get('https://h1bdata.info/index.php?em=&job=data+engineer&city=&year=2022').text
soup=BeautifulSoup(getter,'lxml')
jobs=soup.find_all('table',class_='tablesorter tablesorter-blue hasStickyHeaders')

#write data base in a text file and delete the td and go back to line each etaration

with open('exp.txt', 'w') as f:
    for head in jobs:
        f.write(head.get_text('td').replace('td','\n'))


#transfrom the text file to csv and excel

df=pd.read_fwf('exp.txt')
df.to_csv('exp.csv',index=None)
df.to_excel("testfile.xlsx",index=None)

#get rid of any additional space in the csv file that came from the text file

with open('exp.csv') as input, open('demo1.csv', 'w', newline='') as output:
     writer = csv.writer(output)
     for row in csv.reader(input):
         if any(field.strip() for field in row):
             writer.writerow(row)


#give the csv file the title and delete the 1st six row which are the title itself
Titles=['EMPLOYER','JOB TITLE','BASE SALARY','LOCATION','SUBMIT DATE','START DATE']
df=pd.read_csv('exp.csv',names=Titles)

#deletion of the 6 rows
df=df.iloc[6:]


#transpose every 6 rows in to a columns and delete the 5 rows left that are left voided
transposed_df = pd.DataFrame(columns=df.columns)
for i in range(0, len(df), 6):
    
    transposed_rows = pd.DataFrame(np.array(df.iloc[i:i+6]).T, columns=df.columns)
    
    transposed_df = pd.concat([transposed_df, transposed_rows], ignore_index=True)

#deletion of empty rows
transposed_df.dropna(inplace=True)

#make an end-result csv and excel file
transposed_df.to_csv('your_transposed_file_data.csv', index=False)

transposed_df.to_excel('your_transposed_file_data.xlsx',index=False)





