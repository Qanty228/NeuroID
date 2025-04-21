import numpy as np
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt


x = np.array(range(10))
y = np.random.uniform(low=-1, high=1, size=10)

x_new = np.linspace(x.min(), x.max(), 200)
y_new = np.clip(UnivariateSpline(x, y, s=0.2)(x_new), a_min=-1, a_max=1)

plt.plot(x, y, 'o', label='Исходные точки')
plt.plot(x_new, y_new, '-', label='Кривая')
plt.legend()
plt.show()
