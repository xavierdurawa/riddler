from matplotlib import pyplot as plt
import numpy as np

seq_1 = [1,
2,
4,
6,
12, 
24, 
36, 
48, 
60, 
120,
180,
240,
360,
720,
840]

seq_2 = [1,
2,
3,
4,
6,
8,
9,
10,
12,
16,
18,
20,
24,
30,
32]

s1 = np.array(seq_1)
s2 = np.array(seq_2)

s3 = [s1[i]/2 for i in range(len(s1))]


plt.plot(s3,s2)
plt.show()