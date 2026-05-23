# Lesson: Working with dates Values
import pandas as pd

df = pd.read_csv("Test_csv.csv")
print(df)
print(type(df))

# Add the date column
df['DOJ'] = ['2024-01-01', '2024-01-15', '2024-03-28', '2024-03-03']

# after adding check the date column is in date type or not
print(df['DOJ'].dtype)  # if output is object thne it is not in datatype

# to convert into date updating
df['DOJ'] = pd.to_datetime(df['DOJ'])
print(df['DOJ'].dtype)  # now it is datetime64[ns]

df1 = df
df1['DOJ2'] = ['01-01-2025', '15-01-2025', '28-03-2025', '03-03-2025']
print(df1)
print(df1['DOJ2'].dtype)

# because of not in datetime standard form. It will create big problem while converting into date and time
# For example:
# wil cause error so have use formata
df1['DOJ2'] = pd.to_datetime(df1['DOJ2'], format='%d-%m-%Y')
print(df1['DOJ2'].dtype)


df = df.drop('DOJ2', axis=1)
print(df)

# Extract year
df['Year'] = df['DOJ'].dt.year
print(df)

# Extract month
df['Month'] = df['DOJ'].dt.month
print(df)

# Extract day
df['Day'] = df['DOJ'].dt.day
print(df)

# # adding the time
# df['DOJ'] = df['DOJ'] + pd.Timedelta(days=90)
# print(df)

# Filtering the data
filtered_df = df[(df['Month'] == 1) & (df['Salary'] >= 7000)]
print(filtered_df)

# using chatgpt and get another method
filtered_df_alternative = df.query('Month == 1 and Salary >= 7000')
print(filtered_df_alternative)
