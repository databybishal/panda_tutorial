# Lesson: Parquet file

# import the padans first
import os as os
import pandas as pd
import pyarrow as pa

data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'Paris', 'London']
}

df = pd.DataFrame(data)
print(df)
print(type(df))


# Data converting into parquet file and csv and compare the size

# convert into csv
df.to_csv('toCsv.csv', index=False)
print(df)

df.to_parquet('toParquet.parquet')
print(df)

# checking the size of flie
file_path = 'toCsv.csv'
file_size = os.path.getsize(file_path)
print(file_size)

# checking the size of file
file_path = 'toParquet.parquet'
file_size = os.path.getsize(file_path)
print(file_size)


# Working with parquet file

# Reading whole data from parquet file with engine pyarrow
df = pd.read_parquet('toParquet.parquet', engine='pyarrow',)
print(df)

# Reading specific column data from parquet file with engin pyarrow
df_name_age = pd.read_parquet(
    'toParquet.parquet', engine='pyarrow', columns=['name', 'age'])
print(df_name_age)

#also using filtering
df_name = df_name_age[df_name_age['name'].isin(['Alice', 'Bob'])]
print(df_name)
