import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl as pyxl

#rb = pyxl.load_workbook("result_statistics.xlsx", )
#rb = pd.read_excel("result_statistics.xlsx")

sheet_names = pd.ExcelFile("result_statistics.xlsx").sheet_names

dfs = {}

for sheet in sheet_names:
        dfs[sheet] = pd.read_excel("result_statistics.xlsx", sheet)

ws = dfs['average']

print(ws.index)
#test = pd.DataFrame({"pollution":ws['O₃'], "conc":ws.index})

#sns.distplot(ws['O₃'])

sns.relplot(x = "O₃", y = "PM-10", data = ws)

plt.show()


#ws = rb['average'] #min max

#print(ws.head())