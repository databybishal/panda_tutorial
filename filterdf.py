# Lesson: How to filter the dataframe

# First load the data fro csv
import pandas as pd  # importing the panda lib

# load the csv file and assign the data frame into df
df = pd.read_csv('load.csv')
print(df)  # output of dataframe
print(type(df))  # check if the data frame is dataframe object


# filter the rows according of column condition: (age > 18)
print(df['Age'] >= 18)  # it will give the boolean result
# to get the filter out and get actual data instead of boolean result
df_age_filtered = df[(df['Age'] >= 18) & (df['Salary'] >= 200000)]
print(df_age_filtered)  # also assign it to new dataframe
print(df[df['Age'] >= 18])  # or directly printed the data in print function

# To get the dataframe without any chanage just give the null value or customize the null value with other keyword
df_age_filtered_wcd = df.where(
    ((df['Age'] >= 21)), other='Not Eligible')
print(df_age_filtered_wcd)


