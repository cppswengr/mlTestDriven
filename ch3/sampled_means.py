import matplotlib.pyplot as plt
import numpy as np

plt.title('Distribution of means for N(35,5) distribution '
          '(sampling 100 vs 500 data points)')
plt.xlabel('')
plt.ylabel('Counts')

plt.hist([np.random.normal(loc=35, scale=5, size=100).mean()
          for i in range(2500)], label='100 sample mean')


plt.hist([np.random.normal(loc=35, scale=5, size=500).mean()
          for i in range(2500)], label='500 sample mean')


plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.show