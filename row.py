from itertools import chain
import csv
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

Titles=['EMPLOYER','JOB TITLE','BASE SALARY','LOCATION','SUBMIT DATE','START DATE']



df=pd.read_csv('exp.csv',names=Titles)


df=df.iloc[6:]

# create an empty DataFrame to store the transposed data
transposed_df = pd.DataFrame(columns=df.columns)

# loop through the rows of the original DataFrame in groups of 6
for i in range(0, len(df), 6):
    # select the next 6 rows and transpose them using NumPy
    transposed_rows = pd.DataFrame(np.array(df.iloc[i:i+6]).T, columns=df.columns)
    # add the transposed rows to the new DataFrame
    transposed_df = pd.concat([transposed_df, transposed_rows], ignore_index=True)

transposed_df.dropna(inplace=True)

# write the transposed DataFrame to a new CSV file
transposed_df.to_excel('your_transposed_file.xlsx', index=False)
