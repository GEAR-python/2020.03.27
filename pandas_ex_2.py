import pandas as pd

df = pd.DataFrame({
    'weight' : [91, 85, 100, 75, 43, 38],
    'height' : [180, 173, 190, 170, 163, 152],
    'gender' : ['male','female', 'male', 'female', 'female', 'male']
})

#80 이상이면 True, 아니면 False인 DF 만듬
print(df['weight'] > 80)

#80이상인 값만 남음
df_filtered = df[df['weight']>80]
print(df_filtered)

#weight 기준, 오름차순으로 정렬 = 몸무게 가벼운 순
df_sorted_w = df_filtered.sort_values('weight', ascending=True)
print(df_sorted_w)

#height 기준, 내림차순 정렬 = 키 큰 순
df_sorted_h = df.sort_values('height', ascending = False)
print(df_sorted_h)

#자료를 그룹으로 묶음. 성별에 따라 키와 몸무게 그룹화
df_grouped = df.groupby('gender')
df_grouped_mean = df_grouped.mean()
print(df_grouped_mean)
