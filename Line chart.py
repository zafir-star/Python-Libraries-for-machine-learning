import matplotlib.pyplot as plt
import numpy as np
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
temperature = [22, 24, 23, 26, 25]
plt.plot(days, temperature, marker='o')
plt.title('Weekly Temperature')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.show()