# Lesson: Rows & Columns - Selection

# first load the csv for data
import pandas as pd
df = pd.read_csv('load.csv')
print(df)
print(type(df))

# Select the columns
print(df[['Name']])  # This is single column
print(df[['Name', 'Age']])  # Thie is multiple column

# Select the rowss
print(df.loc[df.Name == 'Bishal'])  # single row with single condition
# single row with multiple condition
print(df.loc[(df.Name == 'Sujan') & (df.Age == 21)])

print(df.loc[df.Age >= 20])  # Multiple row with single condition
print(df.loc[(df.Age >= 22) | (df.Name == 'Komal')])

# Select the row by location of index value
print(df.iloc[0])  # Sinlge row by using index position
# multiple row by using slicing position 
print(df.iloc[0:3])#[start:stop:step] # slicing working like a python where last value would be exclusive and first value inclusive
print(df.loc[0:3]) # in loc both would be inclusive


