import numpy as np
import matplotlib.pyplot as plt
# plt.plot([1,2,3,4])
# plt.plot([1,2,3,4], [1,4,9,16], 'ro')
# plt.ylabel('Some numbers')
# plt.axis([0,6,1,20])

t = np.arange(0,5,0.2)
print(t)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
