import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

age = [random.randint(20, 100) for x in range(0,50)]
weight = [random.randint(40,150) for i in range(0,50)]

df = pd.DataFrame({
    'age': age,
    'weight':weight
})

df.plot(kind='bar', subplots=True)
plt.title('Bar Chart')
plt.savefig('bar_chart_random.png')
plt.show()