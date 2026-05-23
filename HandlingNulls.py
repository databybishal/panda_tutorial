# Lesson: Handling Nulls
import numpy as np
import pandas as pd

df = pd.read_csv("Test_csv.csv")
print(df)
print(type(df))

# making some data null to get the value null
df.loc[df.Name == 'Bishal', 'Salary'] = np.nan
print(df)

# check the null is classic way by boolean output
print(df.isnull())

# check the column how many null according to column
print(df.isnull().sum())

# to remove null to something meaning full  keyword
df = df.fillna(0)
print(df)




