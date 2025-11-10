import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(19.2, 4.8))

X = np.linspace(-3*np.pi, 3*np.pi, 512)

C = np.cos(X)
S = np.sin(X)

plt.plot(X, C, 'r--', label='cos(x)')
plt.plot(X, S, 'b:', label='sin(x)')

plt.title("Cos(x) ja Sin(x) väliltä -3π ... 3π")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.grid(True)
plt.show()
