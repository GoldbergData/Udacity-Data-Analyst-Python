# There are different types of users specified in the "User Type" column.
# Find how many there are of each type and store the counts in a pandas
# Series in the user_types variable.

import pandas as pd

filename = "practice_data.csv"

# load data file into a dataframe
df = pd.read_csv(filename)

# print value counts for each user type
user_types = df["User Type"].value_counts()

print(user_types)

