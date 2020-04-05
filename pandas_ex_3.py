import pandas as pd
df = pd.DataFrame({
    '몸무게':[70, 80, 90, 82, 91],
    '키':[170, 181, 185, 168, 180]
})

#합
total_weight = df['몸무게'].sum()
print(total_weight)

#평균
mean_height = df['키'].mean()
print(mean_height)

#통계값 요약
print(df.describe())

#항목간 상관관계
corr = df.corr()
print(corr)

#csv 파일 읽기
#df = pd.read_csv('my_csv.csv')
#print(df)

#csv 파일 쓰기
#df.to_csv('my_data.csv')