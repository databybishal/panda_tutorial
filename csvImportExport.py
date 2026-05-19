# Lesson: Handling the csv file in pandas

# 3. Save and Load data from csv

import pandas as pd  # frist import the pandas
# print(pd.__version__) for check

data = {
    'Name': ['Bishal', 'Komal', 'Sujan', 'Aayush'],
    'Salary': [2000000, 400000, 560000, 458888,],
    'Age': [23, 20, 21, 22]
}  # This is the data saved in dict form

df = pd.DataFrame(data)  # conver the dict data into dataframe
print(df)  # print the data
print(type(df))  # check if it not dataframe or not

# Save the dataframe into csv  but I have to remove the index
df.to_csv('Test_csv.csv', index=False)


# Import or csv file load
load_df = pd.read_csv('load.csv')
print(load_df) # get a ouptput
print(type(load_df)) # check the dataframe is object or not


