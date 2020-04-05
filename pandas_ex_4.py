import pandas as pd

data = pd.read_csv('data/busan_2010_01.csv', encoding='CP949')
# UnicodeDecodeError 뜨면 위와같이 CP949 적어주면 됨
# 이유 : 파이썬 인코딩 환경 =/ 파일 작성 인코딩 환경

print(data.head(10))

print(data.columns)

data = data.set_index('701')

print(data.describe())

print(data.min())

print(data.max())