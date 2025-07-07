import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
#Dataframe1
data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)
#1
df_average_grade = df1.set_index('Student_ID').mean(axis=1).round(2).reset_index(name = 'Average_grade')
#2
df_max = df_average_grade.set_index('Student_ID').max()
#3
df1['Total'] = df1[['Math','English','Science']].sum(axis=1)
#4
avg_scores = df1[['Math','English','Science']].mean()
plt.Figure(figsize=(8,5))
avg_scores.plot(kind = 'bar',color = 'skyblue')
for index, value in enumerate(avg_scores):
    plt.text(index, value + 1, f'{value:.1f}', ha='center', fontsize=12, color='black')
plt.title('Average grade')
plt.ylabel('Avg grade')
plt.ylim(0,100)
plt.grid(axis ='y',linestyle='--',alpha=0.7)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
#Data_frame2
data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)
#1
df2_sum = df2[['Product_A','Product_B','Product_C']].sum()
#2
df2_max=df2.set_index('Date').sum(axis=1).reset_index('Date').max()
#3
df_pct = df2.copy()
df_pct[['Product_A','Product_B','Product_C']] = (df_pct[['Product_A','Product_B','Product_C']].pct_change()*100).round(1).fillna(100.0)
#4
plt.figure(figsize=(8,5))
ax=df2.plot(kind = 'line',x='Date',marker=0,ax=plt.gca())
products = ['Product_A', 'Product_B', 'Product_C']
colors = ['blue', 'red', 'green'] 

for product, color in zip(products, colors):
    for i, val in enumerate(df2[product]):
        plt.text(df2['Date'][i], val + 1, f'{val}', ha='center', fontsize=9, color=color)

plt.title('Products')
plt.ylabel('Products')
plt.ylim(0,180)
plt.grid(axis ='y',linestyle='--',alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#DateFrame3
data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)
#1
df3.groupby('Department')[['Salary']].mean()
#2
df_most_experience = df3.iloc[df3['Experience (Years)'].idxmax()]
#3
df3.sort_values(by='Salary',inplace=True)
df3['Salary Increase']=(df3['Salary'].pct_change()*100).round(2).fillna(0)
#4
dept_counts = df3.groupby('Department').size().reset_index(name='Count')
plt.figure(figsize=(8,5))
plt.bar(dept_counts['Department'], dept_counts['Count'], color='skyblue')
for index, value in enumerate(dept_counts['Count']):
    plt.text(index, value + 0.2, f'{value}', ha='center', fontsize=11, color='black')
plt.title('Department count')
plt.ylabel('Count')
plt.grid(axis='y',linestyle='--',alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#DataFrame4
data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)
#1
total_revenue = df4['Total_Price'].sum()
#2
top_prod = df4.groupby('Product')['Quantity'].sum().idxmax()
print(f'🍕 Наиболее заказываемый продукт: {top_prod}')
#3
average_quantity = df4['Quantity'].mean()
print(f'📦 Среднее количество заказанных продуктов: {average_quantity:.2f}')
#4
plt.figure(figsize=(8,5))
product_sum = df4.groupby('Product')['Total_Price'].sum()
plt.pie(product_sum, labels=product_sum.index, autopct='%1.1f%%', startangle=140)
plt.title('Распределение оборота по продуктам')
plt.tight_layout()
plt.show()
