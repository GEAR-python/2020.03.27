# numpy는 일반적인 list 계산보다 3~40배 빠르다

import numpy as np

a = np.array([
    [1,2],
    [3,4],
    [5,6]
])

# 행열 정보 및 성분 추출 
print(a.shape)
print(a[0,1])

# 조건을 적용할 수 있다.
bool_idx = (a > 2)
print(bool_idx)

# 2보다 큰값만 출력
print(a[ a>2 ])

# 행열끼리 사칙연산
b = np.array([
    [10,11],
    [12,13],
    [13,14]
])

print(a+b)
print(np.add(a,b))

print(a-b)
print(np.subtract(a,b))

print(a*b)
print(np.multiply(a,b))

print(a/b)
print(np.divide(a,b))

#행, 열끼리 더하기
x = np.array([[1,2,3], [4,5,6]])
print(np.sum(x, axis=0)) # 열(column) 끼리 값을 더합니다.
print(np.sum(x, axis=1)) # 행(row)끼리 값을 더합니다.
