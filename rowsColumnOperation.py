# Lession: Operation in rows and column in dataframe
import pandas as pd

df = pd.read_csv("Test_csv.csv")
print(df)

# How to add column

# adding column simply using list
df['Team'] = ['CEO', 'HR', 'CTO', 'DA']
print(df)

# also can add column by perform the operation
df['Bonus'] = df['Salary'] * 0.2
print(df)

# add new row at the end of dataframe
df.loc[len(df)] = ['Biswash', 2000000, 22, 'Employeer', 20000.0]
print(df)
print(len(df))


# update value by index
df.loc[0, 'Salary'] = 950000
print(df)

# update value - Using column name
df.loc[df.Name == 'Biswash', 'Salary'] = 20000
print(df)

# delete value - row and columns values

# by default rows delete because axis assign always zero
# for row directly not deleting in orginal dataframe, If I used inpalce=True then it will directly drop in original dataframe
new_df = df.drop(df[df.Name == 'Komal'].index)
print(new_df)

# can also deleted using index by rows if single directly value if multiple can be give as list
new_column_drop_index = df.drop([1, 2, 3, 4], axis=0)
print(new_column_drop_index)

# column: Have to change axis for it
new_column_drop = df.drop('Bonus', axis=1)
print(new_column_drop)

# multiple column delete
new_multiple_Drop_column = df.drop(['Age', 'Name'], axis=1)
print(new_multiple_Drop_column)

# Sort according to ascending and descindings

# ascending order
sort_salary_asc = df.sort_values('Salary')
print(sort_salary_asc)

# descending
sort_salary_desc = df.sort_values('Salary', ascending=False)
print(sort_salary_desc)



