import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)  # Generate an array of values.
y = np.sin(x)  # Calculate y values.

plt.plot(x, y)
plt.show()