import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0, 10, 0.1)

amp = np.sin(time)
amp2 = np.cos(time)


plt.figure(figsize = (16,8))
plt.plot(time, amplitude)
plt.plot(time, amplitude2+3)
plt.plot(time, amplitude2*3)

plt.xticks([])
plt.yticks([])


mplcyberpunk.add_glow_effects()

plt.show()
