import pandas as pd
import matplotlib.pyplot as plt
import  numpy as np
df = pd.read_csv('gy_link_travel_time_part1.txt', delimiter=';', dtype={'link_ID': object})

fig, axes = plt.subplots(nrows=2, ncols=1)
df['travel_time'].hist(bins=100, ax=axes[0])
df['travel_time'] = np.log1p(df['travel_time'])
df['travel_time'].hist(bins=100, ax=axes[1])
plt.savefig('3_1.png')

#plt.show()