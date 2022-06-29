import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax3d = fig.add_subplot(1, 2, 1, projection='3d')

# data
x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(x, y)

# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)

# Z  = X / (X**2+Y**2)
# Z = 0.1 * np.cos ( ( X**2+Y**2) / 4.0 ) / ( 3 * X**2+Y**2) 
Z = np.exp((-X**2-Y**2))


# Plot 
surf = ax3d.plot_surface(X, Y, Z, cmap='plasma', linewidth=0)

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

a = X.flatten()
b = Y.flatten()
c = Z.flatten()

axh = fig.add_subplot(1, 2, 2)
axh.hist2d(a, b, weights=c, cmap='plasma')
plt.show()
