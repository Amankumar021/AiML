import pandas as pd

# df = pd.read_json("sample_Data.json")

data = {
    "Name": ['shyaM','aMAN','SHAKAR'],
    "Age" : [10,20,30],
    "City" : ['nagpur', 'mumbai ', 'delhi']
}

df = pd.DataFrame(data)

print('Displaying the info of data set')

print(df.info())