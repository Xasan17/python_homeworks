import pandas as pd 
df = pd.read_csv('stackoverflow_qa.csv')
df1 = pd.read_csv('titanic.csv')
#homework 2 
#1
df['creationdate'] = pd.to_datetime(df.creationdate)
df_to_2014 = df[df.creationdate.dt.year<2014] 
#2
high_score_50questions = df[df['score']>50]
#3
high_score_50_100questions = df[df['score'].between(50,100)]
#4
ans_Scott = df[df.ans_name=='Scott Boston']
#5
users = ['Scott Boston', 'Demitri', 'doug', 'Mike Pennington', 'Wes McKinney']
ans_5users = df[df['ans_name'].isin(users)]
#6
df_filter = df[(df.creationdate.dt.year==2014) & (df.creationdate.dt.month.between(3,10)) & (df.ans_name == 'Unutbu') & (df.score<5)]
#7
df_score = df[(df.score.between(5,10)) | (df.viewcount>10000)]
#8
no_ans_Scott = df[df.ans_name!='Scott Boston']
#homework 3
#1
df_female_class1_20_30 = df1[
    (df1['Sex'] == 'female') &
    (df1['Pclass'] == 1) &
    (df1['Age'].between(20, 30))
]
#2
df_fare_over_100 = df1[df1['Fare'] > 100]
#3
df_survived_alone = df1[
    (df1['Survived'] == 1) &
    (df1['SibSp'] == 0) &
    (df1['Parch'] == 0)
]
#4
df_embarked_c_fare50 = df1[
    (df1['Embarked'] == 'C') &
    (df1['Fare'] > 50)
]
#5
df_family_abroad = df1[
    (df1['SibSp'] > 0) &
    (df1['Parch'] > 0)
]
#6
df_child_not_survived = df1[
    (df1['Age'] <= 15) &
    (df1['Survived'] == 0)
]
#7
df_cabin_fare200 = df1[
    df1['Cabin'].notna() & 
    (df1['Fare'] > 200)
]
#8
df_odd_passenger_id = df1[df1.PassengerId % 2 == 1]
#9
df_unique_tickets = df1[df1['Ticket'].duplicated(keep=False) == False]
#10
df_miss_class1 = df1[
    (df1['Sex'] == 'female') &
    (df1['Pclass'] == 1) &
    (df1['Name'].str.contains('Miss', case=False))
]
