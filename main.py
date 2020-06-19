import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 11, num=200, endpoint=False)
y = np.cos(x)

plt.plot(y)
plt.show()
