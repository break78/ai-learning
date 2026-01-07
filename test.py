import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 500)
signal = np.sin(2 * np.pi * 5 * t)
noise = 0.2 * np.random.randn(len(t))
noisy_signal = signal + noise

plt.plot(t, noisy_signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Noisy Sine Wave")
plt.show()
