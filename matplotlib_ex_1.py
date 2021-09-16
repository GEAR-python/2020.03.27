import numpy as np
import matplotlib.pyplot as plt


print('test')

#간단한 직선 그래프 그리기
x_1 = [1,2,3]
y_1 = [0,1,2]

#plt.plot(x_1,y_1)
#plt.show()

#사인 곡선 그리기
x_2 = np.arange(0,10, 0.1)
print(x_2)

y_2 = np.sin(x_2)

#plt.plot(x_2, y_2)
#plt.show()

#여러 그래프 같이 그리기
t = np.arange(0., 10., 0.2)

plt.plot(t, t, 'r--', #3번째는 그래프 형식(모양)
         t, 2*t, 'bs',
         t, t**2,'g^')


plt.title('several graphs')
plt.show()