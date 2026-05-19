# Lesson: Dataframe

# Create a Dataframe
import pandas as pd  # importing the pandas lib
# print(pd.__version__) # just for checking

# use DataFrame method for create a dataframe
# using list
df = pd.DataFrame([["Bishal", "Komal"], [23, 45]], columns=['Name', 'Age'])
print(df)  # print the dataframe that created
print(type(df))  # to check it is dataframe or not

# Using the dict for make dataframe
data = {
    'Name': ['bishal', 'sujan', 'komal', 'aayush'],
    'Age': [21, 24, 22, 34],
    'Salary': [90000, 70000, 500000, 465756476]
}

df = pd.DataFrame(data)  # using method for dataframe
print(df)  # printing the dataframe created
print(type(df))  # type of the dataframe check


# 2. Basic Dataframe Understanding
# first is head and tail method will give top and down rows which can be can be customize by giving number paramter. Default (5 rows)
# head
print(df.head(3))  # top three data

# tail
print(df.tail(3))  # bottom three data

# shape
# first number of rows and number of columns of dataframe in (4, 3) tuple format
print(df.shape)

# To get the what are the columns are ?
print(df.columns)

# To change the name of columns ? Do not change the value in this line have use inplace to directly change in this line
df.rename(columns={'Salary': 'Monthly_Salary'}, inplace=True)
print(df)


# To chec the info of dataframe
df.info()  # Will return dtatype, Non_NULl Count Dtype column name, memory usage, everthing information of dataframe

# to see the information and statistical summary of dataframe on the measurable data column, with (count, mean, std, min, 25%, 50%, 75%, max)
print(df.describe())
