import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(19.2, 4.8))

X = np.linspace(-3*np.pi, 3*np.pi, 300)
C = np.cos(X)
S = np.sin(X)

plt.plot(X, C, 'r--', label='cos(x)')
plt.plot(X, S, 'b:', label='sin(x)')
plt.legend()

plt.title("Cos(x) ja Sin(x) väliltä -3π ... 3π")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)

ticks = [-3*np.pi, -2*np.pi, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 2*np.pi, 3*np.pi]
tick_labels = [r'$-3\pi$', r'$-2\pi$', r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$',
               r'$\frac{\pi}{2}$', r'$\pi$', r'$2\pi$', r'$3\pi$']

plt.show()
