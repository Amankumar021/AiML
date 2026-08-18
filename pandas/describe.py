import pandas as pd

data ={
    "Name ": ['Ram', 'shyam', 'shubaham','aman', 'ankit', 'shubh', 'aditya', 'ankur'],
    "Age" : [30,20,50, 18,19,30,22,25],
    "Salary" : [100000,48000,15000,25000,60000,50000,35000,25000],
    "performance Score" : [80,82,80,75,60,95,35,60]
}

df = pd.DataFrame(data)

print ("Sample Dataframe")
print(df)

print('Descriptive statistics')
print(df.describe()) #