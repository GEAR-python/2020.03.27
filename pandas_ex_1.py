import pandas as pd

df = pd.DataFrame({
    'name':['Bob', 'Alice', 'June'],
    'age':[71, 33, 58]
})

print(df)

# (3,2) 출력. 3행 2열의 데이터 프레임이란 뜻.
print(df.shape)

#열(column) 별로 데이터 이용
print(df['age'])
print(df['name'])

#행 별로 데이터 이용 (index로 범위지정)
print(df[:1])

print(df.index)
print(df.columns)
