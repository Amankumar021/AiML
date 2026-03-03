import pandas as pd

data = {
    "Name": ['shyaM','aMAN','SHAKAR'],
    "Age" : [10,20,30],
    "City" : ['nagpur', 'mumbai ', 'delhi']
}

df = pd.DataFrame(data)

print(df)

# df.to_csv("output.csv", index=False) #to save csv file

df.to_excel("output.xlsx")
df.to_json("output.json", index = False)