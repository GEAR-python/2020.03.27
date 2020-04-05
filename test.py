import pandas as pd

file_name = "data/측정기록지(2010년1월).xlsx"
df = pd.read_excel(file_name)

print(df)