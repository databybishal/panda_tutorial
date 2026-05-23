# Lesson: Concatenate & Merge DataFrames(JOINs)
import pandas as pd

# first create two dataframe (df1 and df2)
df1 = pd.DataFrame({'Id': [1, 2, 3], 'Name': ['A', 'B', 'C']})
df2 = pd.DataFrame({'Ids': [1, 2, 2], 'Score': [89, 96, 77]})
print(df1)
print(df2)


# concatenation
# it will provide NaN do not match anything it is just concatenation
df_concat_rowLevel = pd.concat([df1, df2], axis=0)  # row level  concatenate
print(df_concat_rowLevel)

df_concat_columnsLevel = pd.concat(
    [df1, df2], axis=1)  # columns level  concatenate
print(df_concat_columnsLevel)


# Merge or Join (Inner join, Left Join, Right Join, Outer Join)
# if the join of column name is same  if the use left_on and right_on
df_inner_join = pd.merge(df1, df2, how='inner', left_on='Id', right_on='Ids')
print(df_inner_join)


# Using chat
