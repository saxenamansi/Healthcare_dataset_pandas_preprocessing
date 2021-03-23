import pandas as pd
df = pd.read_csv('healthcare-stroke.csv')

#TASK 1: Inspect the data frame with statistics
print(df.head(10))
print(df.tail(10))
print(df.info())
print(df.describe())


#TASK 2: Parse the data frame or series using specific column and condition
# 1. Displaying those rows that have age greater than 50
print(df[df['age'] > 50])
# 2. Displaying those rows that have heart disease
print(df[df['heart_disease'] ==1])
# 3. Displaying the rows that do not have hypertension
print(df[df['hypertension'] == 0])
# 4. Displaying those rows that have heart disase and age greater than 40
print(df[((df['age'] > 40) & (df['heart_disease'] == 1))])
# 5. Displaying those rows that have hypertension and no heart disease 
print(df[((df['hypertension'] ==1) & (df['heart_disease'] == 0))])

#TASK 3: Find Missing values from the dataset 
null = df.isna().sum()
print("Number of null values in the dataset are: ", null)


#TASK 4: Parse the row without NaN
print(df.dropna())


#TASK 5: Fill the missing data with default value, forward fill, backward fill, and with mean of the column
# 1. Filling null values with default value 0
print(df.fillna(20))
# 2. Filling null values with forward fill
print(df.fillna(method = "ffill"))
# 3. Filling null values with backward fill
print(df.fillna(method = "bfill"))
# 4. Filling null value with mean of bmi column
print(df.fillna(df['bmi'].mean()))
# 5. Filling null value with median of bmi column
print(df.fillna(df['bmi'].median()))
# 6. Filling null value with mode of bmi column
print(df.fillna(df['bmi'].mode()))
