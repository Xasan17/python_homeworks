import pandas as pd 
#Homework1
df = pd.read_csv(r'task\sales_data.csv')
df.head(5)
#1
result1 = df.groupby('Category').agg({'Quantity':['sum','max'],'Price': 'mean'})
result1.columns = ['Total_Quantity', 'Max_Quantity', 'Average_Price']
result1.reset_index(inplace=True)
print(result1)
#2
grouped2 = df.groupby(['Category','Product'])['Quantity'].sum().reset_index()
result2 = grouped2.loc[grouped2.groupby('Category')['Quantity'].idxmax()].reset_index(drop=True)
print(result2)
#3
df['Revenue'] = df.Quantity*df.Price
grouped3 = df.groupby('Date')['Revenue'].sum().reset_index()
max_revenue_date = grouped3.loc[grouped3['Revenue'].idxmax()]
print(max_revenue_date)
#Homework2
df1 = pd.read_csv(r'task\customer_orders.csv')
df1.head()
#1
grouped4 = df1.groupby('CustomerID')['OrderID'].count().reset_index()
top_counts = grouped4[grouped4['OrderID']>20]
top_counts.columns = ['CustomerID','Count_Orders']
print(top_counts)
#2
grouped5 = df1.groupby('CustomerID')['Price'].mean().reset_index()
grouped5.columns = ['CustomerID','AVG_Price']
price_mean = grouped5[grouped5['AVG_Price']>120]
print(price_mean)
#3
grouped6 = df1.groupby('Product').agg({'Quantity':'sum','Price':'sum'}).reset_index()
grouped6.columns = ['Product','Total_quantity','Total_price']
quant_price = grouped6[grouped6['Total_quantity']>=5]
print(quant_price)
#Homework3
#1
import sqlite3
with sqlite3.connect(r'task\population.db') as conn:
    population_df = pd.read_sql_query('select * from population',conn)
#2
def group_salary(s):
    i=200_000
    t=0
    while True:
        if s<i:
            return t
        i+=200_000
        t+=1
        if i>1_800_000:
            return t
            
population_df['group_salary']=population_df['salary'].apply(group_salary)
population_salary_df = pd.read_excel(r'task\population_salary_analysis.xlsx')
population_salary_df['Average Salary']= population_df.groupby('group_salary')['salary'].agg('mean').round(0)
population_salary_df['Median Salary'] = population_df.groupby('group_salary')['salary'].agg('median').round(0)
population_salary_df['Number of population'] = population_df.groupby('group_salary')['salary'].agg('count').round(0)
population_salary_df['Percentage'] = ((population_salary_df['Number of population'] / population_df['id'].count())*100).round(0)
population_salary_df.to_excel(r'task\population_salary_analysis.xlsx', index=False)
#3
grouped = population_df.groupby(['group_salary', 'state'])['salary'].agg(
    Average_Salary='mean',
    Median_Salary='median',
    Number_of_population='count'
).round(0)
total_population = len(population_df)
grouped['Percentage'] = (grouped['Number_of_population'] / total_population * 100).round(0)
population_state_salary_df = grouped.reset_index()
