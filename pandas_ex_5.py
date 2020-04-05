import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/milk.csv')

data = data.set_index('year')
grouped_dairy = data.groupby('dairy')

for key, group in grouped_dairy:
    group_sorted = group.sort_values('year',
    ascending = True)

    group_sorted.plot(kind='bar', subplots = False)

    plt.legend(['production', 'comsumption'])
    plt.xlabel(key)

    plt.savefig('milk_graph_{}.png'.format(key))

plt.show()
plt.close()