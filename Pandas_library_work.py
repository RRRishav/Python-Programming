#Pandas is used for data analysis

import pandas as pd
print("Introduction to the pandas")



# key datastructure in pandas  -> Series and dataframe

#series->1d
# dataframe -> 2d

s = pd.Series([1,2,3,4])
s


df = pd.read_csv("/content/sample_data/california_housing_test.csv")
df
