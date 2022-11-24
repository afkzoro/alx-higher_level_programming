import control as cnt
import numpy
from matplotlib import pyplot as plt

s = cnt.tf('s')
G = 1/(s + 2)
t, y = cnt.step_response(5 * G)

# Plotting

plt.figure(1)
plt.plot(t, y, 'b', linewidth=3, label='Step Response')
plt.xlabel('Time (sec)')
plt.ylabel('Response (y)')
plt.legend(loc='center right')
plt.show()
