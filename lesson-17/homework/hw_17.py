import pandas as pd
import numpy as np
# homework 1
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
#1
df.rename(columns={'First Name':'first name', 'Age': 'age'},inplace=True)
#2
df.head(3)
#3
df['age'].mean()
#4
print(df[['first name','City']])
#5
df['salary']=np.random.randint(5_000_000,15_000_001, size=len(df))
#6
df.describe()
# homework 2
dict_df = {'Month':['Jan','Feb','Mar','Apr'],
           'Sales':[5000,6000,7500,8000],
           'Expenses': [3000,3500,4000,4500]} 

sales_and_expenses = pd.DataFrame(dict_df)
#1
print(f'Sales max: {sales_and_expenses['Sales'].max()}')
print(f'Expenses max: {sales_and_expenses['Expenses'].max()}')
#2
print(f'Sales min: {sales_and_expenses['Sales'].min()}')
print(f'Expenses min: {sales_and_expenses['Expenses'].min()}')
#3
print(f'Sales mean: {sales_and_expenses['Sales'].mean()}')
print(f'Expenses mean: {sales_and_expenses['Expenses'].mean()}')
# homework 3
#1
category_dict = {'Category':['Rent','Utilities','Groceries','Entertainment'],
                 'January' :[1200,200,300,150],
                 'February':[1300,220,320,160],
                 'March' :[1400,240,330,170],
                 'April' :[1500,250,350,180]}
df1 = pd.DataFrame(category_dict)
df1.set_index('Category',inplace=True)
#2
print(f'Max by category: {df1.max(axis=1)}')
#3
print(f'Min by category: {df1.min(axis=1)}')
#4
print(f'Mean by category: {df1.mean(axis=1)}')



