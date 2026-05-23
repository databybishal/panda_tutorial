# Lesson: Aggregation and Group by
import pandas as pd
df = pd.read_csv('Test_csv.csv')
print(df)
print(type(df))

# add the date
df['DOJ'] = ['2024-01-01', '2024-01-15', '2024-03-28', '2024-03-03']
print(df['DOJ'].dtype)
df['DOJ'] = pd.to_datetime(df['DOJ'])
print(df['DOJ'].dtype)
df['Year'] = df['DOJ'].dt.year
print(df)
df['Month'] = df['DOJ'].dt.month
print(df)
df['Day'] = df['DOJ'].dt.day
print(df)
# count the value according to the value
count_people = df[df['Month'] == 1].value_counts()
print(count_people)


# group the some by month
print(df.groupby('Month')['Salary'].sum())

#working with multiple aggregation with group by
print(df.groupby('Month').agg({'Salary': 'mean', 'Name':'count'}))


