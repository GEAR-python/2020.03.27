import pandas as pd
import numpy as np


df = pd.DataFrame([[1.4, np.nan], [7.1,-4.5],[np.nan, np.nan],[0.75,-1.3]],
index=['a','b','c','d'],
columns=['one','two'])

print(df)

print(df.sum())
print(df.sum(axis=1, skipna = True))