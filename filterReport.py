import csv
import pandas as pd
from pandas import DataFrame

data = pd.read_csv('ComplianceReport.csv', index_col = 0, usecols=['NodeName', 'NodeIpAddress', 'No public Community String'])
df = data
print(data.head())
#Remove any data that inlcudeds Passwed in the specified column 
select_snmp =  df.loc[df['No public Community String'] != 'Passed']
print(select_snmp)
#Write pulled data to new CSV file
#Example https://datatofish.com/select-rows-pandas-dataframe/
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
select_snmp.to_csv('testReport.csv')